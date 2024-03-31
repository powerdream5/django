from django.test import TestCase
from team.forms import TeamMemberForm
from team.models import TeamMember

class TeamMemberFormTest(TestCase):

    def test_clean_first_name_empty(self):
        # Test that the form raises a validation error when first name is empty
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone': '(123) 456-7890',
            'role': TeamMember.REGULAR
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(form.errors['first_name'], ['This field is required.'])

    def test_clean_last_name_empty(self):
        # Similar test for last_name
        form_data = {
            'first_name': 'John',
            'last_name': '',
            'email': 'johndoe@example.com',
            'phone': '(123) 456-7890',
            'role': TeamMember.REGULAR
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)

    def test_clean_email_empty(self):
        # Test for empty email
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': '',
            'phone': '(123) 456-7890',
            'role': TeamMember.REGULAR
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_clean_email_duplicate(self):
        # First, create a TeamMember to test against
        TeamMember.objects.create(first_name='John', last_name='Doe', email='johndoe@example.com', phone='(123) 456-7890', role=TeamMember.REGULAR)
        
        # Then test submitting a form with the same email
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'johndoe@example.com',  # Same email as the existing user
            'phone': '(321) 654-0987',
            'role': TeamMember.ADMIN
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['A team member with this email already exists.'])

    def test_form_valid(self):
        # Test the form with valid data
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'janedoe@example.com',
            'phone': '(123) 456-7890',
            'role': TeamMember.REGULAR
        }
        form = TeamMemberForm(data=form_data)
        self.assertTrue(form.is_valid())
