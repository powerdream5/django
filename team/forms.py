from django import forms
from .models import TeamMember
from django.core.validators import RegexValidator

class TeamMemberForm(forms.ModelForm):
    first_name = forms.CharField(
        error_messages={'required': 'First name cannot be empty.'}
    )
    last_name = forms.CharField(
        error_messages={'required': 'Last name cannot be empty.'}
    )
    email = forms.EmailField(
        error_messages={'required': 'Email cannot be empty.'}
    )

    role = forms.ChoiceField(choices=TeamMember.ROLE_CHOICES, widget=forms.RadioSelect)
    
    phone_regex = RegexValidator(regex=r'^\(\d{3}\) \d{3}-\d{4}$', message="Phone number must be entered in the format: '(999) 999-9999'.")
    phone = forms.CharField(validators=[phone_regex], max_length=17, error_messages={'required': 'Phone number cannot be empty.'})

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email').lower().strip()
        
        # Check if the email already exists in the database
        if TeamMember.objects.filter(email__iexact=email, is_deleted=False).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('A team member with this email already exists.')

        return email
