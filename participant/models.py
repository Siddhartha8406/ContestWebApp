from django.db import models

class Team(models.Model):
    dept_choices = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]

    team_id = models.AutoField(primary_key=True, unique=True)
    team_name = models.CharField(max_length=50)
    team_college = models.CharField(max_length=50)
    team_department = models.CharField(max_length=3, choices=dept_choices)

    project_name = models.CharField(max_length=50, default="Project Name Here")
    project_description = models.CharField(max_length=100, default="Project Description Here")
    project_video_url = models.CharField(max_length=100, default="")
    project_source_code = models.CharField(max_length=100, default="")

    project_image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.png')