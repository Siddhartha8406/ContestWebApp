# Generated by Django 4.2.1 on 2023-06-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("participant", "0002_alter_team_team_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_source_code",
            field=models.CharField(default="Source Code Here", max_length=100),
        ),
        migrations.AddField(
            model_name="project",
            name="project_video_url",
            field=models.CharField(default="Video URL Here", max_length=100),
        ),
    ]