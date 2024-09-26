from django import forms
from .models import EmployerProfile

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'company_name',
            'company_description',
            'company_logo',
            'website',
            'address',
            'contact_number',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Description'}),
            'company_logo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
        }
        labels = {
            'company_name': 'Company Name',
            'company_description': 'Company Description',
            'company_logo': 'Company Logo',
            'website': 'Website',
            'address': 'Company Address',
            'contact_number': 'Contact Number',
        }


from .models import JobPosting

from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = [
            'title',
            'description',
            'location',
            'required_skills',  # Keep this field for skills description
            'salary',
            'deadline',
            'job_type'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Location'}),
            'required_skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter required skills (comma-separated)'}),  # Use Textarea for skills
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
        }
