# Generated by Django 4.2.2 on 2024-02-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0008_alter_studentregister_korean_select_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specify",
            name="content",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="studentregister",
            name="korean_select",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="studentregister",
            name="math_select",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="studentregister",
            name="research1_select",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="studentregister",
            name="research2_select",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="studentregister",
            name="research3_select",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
