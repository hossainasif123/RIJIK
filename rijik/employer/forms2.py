from django import forms
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
