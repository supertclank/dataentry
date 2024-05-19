from django import forms
from models.models import Job, Document

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Job_Name', 'Job_Description']
        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['Name', 'Description', 'Document_file']