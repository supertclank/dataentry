from django import forms
from models.models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Job_Name', 'Job_Description']