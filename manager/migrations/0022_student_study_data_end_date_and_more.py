# Generated by Django 4.2.2 on 2024-01-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0021_student_study_data_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student_study_data",
            name="end_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="student_study_data",
            name="start_date",
            field=models.DateField(null=True),
        ),
    ]
