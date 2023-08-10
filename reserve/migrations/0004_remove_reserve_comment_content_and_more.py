# Generated by Django 4.2.2 on 2023-07-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reserve", "0003_notice"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserve",
            name="comment_content",
        ),
        migrations.RemoveField(
            model_name="reserve",
            name="comment_subject",
        ),
        migrations.AddField(
            model_name="reserve",
            name="comment",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]