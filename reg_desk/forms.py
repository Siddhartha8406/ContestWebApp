from django import forms
from django.forms import ModelForm
from participant.models import Team

class TeamForm(ModelForm):
    dept_choices = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]

    team_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Team Name', 'id':'team_name', 'class':'form_elements'}))

    team_college = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'College', 'id':'team_college', 'class':'form_elements'}))

    team_department = forms.ChoiceField(choices=dept_choices, widget=forms.Select(attrs={'id':'team_department', 'class':'form_elements'}))
    
    class Meta:
        model = Team
        fields = ['team_name', 'team_college', 'team_department']