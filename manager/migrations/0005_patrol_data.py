# Generated by Django 4.2.2 on 2023-06-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0004_alter_student_study_data_english_lecture_study_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patrol_Data",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("week_name", models.CharField(max_length=255, null=True)),
                ("student_name", models.CharField(max_length=255)),
                ("k_ss_count", models.IntegerField(blank=True, null=True)),
                ("k_il_count", models.IntegerField(blank=True, null=True)),
                ("m_ss_count", models.IntegerField(blank=True, null=True)),
                ("m_il_count", models.IntegerField(blank=True, null=True)),
                ("e_ss_count", models.IntegerField(blank=True, null=True)),
                ("e_il_count", models.IntegerField(blank=True, null=True)),
                ("r_ss_count", models.IntegerField(blank=True, null=True)),
                ("r_il_count", models.IntegerField(blank=True, null=True)),
                ("plan", models.IntegerField(blank=True, null=True)),
                ("mentoring", models.IntegerField(blank=True, null=True)),
                ("question", models.IntegerField(blank=True, null=True)),
                ("consulting", models.IntegerField(blank=True, null=True)),
                ("sleep", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
