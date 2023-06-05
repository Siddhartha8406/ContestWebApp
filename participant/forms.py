from django import forms
from django.forms import ModelForm
from .models import Team

class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Project Name', 'id':'project_name', 'class':'form_elements'}))
    project_description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Project Description', 'id':'project_description', 'class':'form_elements'}))
    project_image = forms.ImageField(widget=forms.FileInput(attrs={'id':'project_image', 'class':'form_elements', 'name':'project_image', "required":"False"}))

    class Meta:
        model = Team
        fields = ('project_name', 'project_description', 'project_image')
