# Generated by Django 5.0.7 on 2024-07-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elnara", "0004_certificates_projects_delete_certificate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="video",
            field=models.FileField(default="default_video.mp4", upload_to="projects/"),
        ),
    ]