# Generated by Django 4.2.1 on 2023-06-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("participant", "0004_team_project_description_team_project_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="project_image",
            field=models.ImageField(default="images/default.jpg", upload_to="images/"),
        ),
    ]
