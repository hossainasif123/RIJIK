from django import forms
from .models import JobSeekerProfile, Skill
from django.forms import formset_factory
class JobSeekerProfileForm(forms.ModelForm):
    # Customizing the skills field to allow selecting multiple options
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required=False
    )

    # Adding fields for additional information
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'})
    )

    education_level = forms.ChoiceField(
        choices=[
            ('secondary', 'Secondary'),
            ('higher_secondary', 'Higher Secondary'),
            ('graduation', 'Graduation'),
            ('post_graduation', 'Post Graduation'),
            ('others', 'Others')
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    github_link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'GitHub URL'})
    )

    linkedin_link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn URL'})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'})
    )

    religion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Religion'})
    )

    nationality = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'})
    )

    nid_no = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NID Number'})
    )

    blood_group = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blood Group'})
    )

    previous_experience = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Previous work experience'})
    )

    class Meta:
        model = JobSeekerProfile
        fields = [
            'name',
            'resume',
            'portfolio',
            'skills',
            'experience',
            'education',
            'education_level',
            'location',
            'availability',
            'desired_salary',
            'github_link',
            'linkedin_link',
            'email',
            'date_of_birth',
            'religion',
            'nationality',
            'nid_no',
            'blood_group',
            'previous_experience'
        ]
        widgets = {
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'portfolio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Portfolio URL'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Job experience'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Educational background'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your location'}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Full-time, Part-time'}),
            'desired_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desired salary'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new skill'}),
        }
SkillFormSet = formset_factory(SkillForm, extra=3) 