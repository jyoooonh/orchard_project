# Generated by Django 4.2.2 on 2023-07-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0006_rename_week_name_patrol_data_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="patrol_data",
            name="focus_one",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patrol_data",
            name="focus_three",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patrol_data",
            name="focus_two",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patrol_data",
            name="total_focus_count",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
