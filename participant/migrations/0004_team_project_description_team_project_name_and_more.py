# Generated by Django 4.2.1 on 2023-06-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("participant", "0003_project_project_source_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="project_description",
            field=models.CharField(default="Project Description Here", max_length=100),
        ),
        migrations.AddField(
            model_name="team",
            name="project_name",
            field=models.CharField(default="Project Name Here", max_length=50),
        ),
        migrations.AddField(
            model_name="team",
            name="project_source_code",
            field=models.CharField(default="Source Code Here", max_length=100),
        ),
        migrations.AddField(
            model_name="team",
            name="project_video_url",
            field=models.CharField(default="Video URL Here", max_length=100),
        ),
        migrations.AlterField(
            model_name="team",
            name="team_college",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="team",
            name="team_department",
            field=models.CharField(
                choices=[
                    ("CSE", "Computer Science and Engineering"),
                    ("ECE", "Electronics and Communication Engineering"),
                    ("EEE", "Electrical and Electronics Engineering"),
                    ("ME", "Mechanical Engineering"),
                ],
                max_length=3,
            ),
        ),
        migrations.DeleteModel(name="Project",),
    ]
