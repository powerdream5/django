from django import forms
from .models import TeamMember
from django.core.validators import RegexValidator

class TeamMemberForm(forms.ModelForm):
    role = forms.ChoiceField(choices=TeamMember.ROLE_CHOICES, widget=forms.RadioSelect)
    phone_regex = RegexValidator(regex=r'^\(\d{3}\) \d{3}-\d{4}$', message="Phone number must be entered in the format: '(999) 999-9999'.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone', 'role']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('This field cannot be empty.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('This field cannot be empty.')
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email').lower().strip()  # Normalize the email
        if not email:
            raise forms.ValidationError('This field cannot be empty.')

        # Check if the email already exists in the database
        if TeamMember.objects.filter(email__iexact=email, is_deleted=False).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('A team member with this email already exists.')

        return email
