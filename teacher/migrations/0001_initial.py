# Generated by Django 4.2.2 on 2023-06-24 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Consulting",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("date", models.DateField(blank=True, null=True)),
                ("subject", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "student_name",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "consulting_type",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "consulting_subject",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "consulting_content",
                    models.TextField(blank=True, max_length=2000, null=True),
                ),
                (
                    "teacher_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
