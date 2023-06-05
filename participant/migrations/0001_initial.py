# Generated by Django 4.2.1 on 2023-06-04 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                ("team_id", models.AutoField(primary_key=True, serialize=False)),
                ("team_name", models.CharField(max_length=50)),
                ("team_department", models.CharField(max_length=50)),
                (
                    "team_college",
                    models.CharField(
                        choices=[
                            ("CSE", "Computer Science and Engineering"),
                            ("ECE", "Electronics and Communication Engineering"),
                            ("EEE", "Electrical and Electronics Engineering"),
                            ("ME", "Mechanical Engineering"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "project_name",
                    models.CharField(default="Project Name Here", max_length=50),
                ),
                (
                    "project_description",
                    models.CharField(
                        default="Project Description Here", max_length=100
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="participant.team",
                    ),
                ),
            ],
        ),
    ]