# Generated by Django 4.2.2 on 2024-02-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0031_weekplan_fri_date_weekplan_mon_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weekplan",
            name="fri_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="fri_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="mon_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sat_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="sun_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="thu_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="tue_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_english_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_english_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_english_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_english_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_korean_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_korean_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_korean_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_korean_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_math_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_math_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_math_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_math_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_research_lecture_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_research_lecture_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_research_self_study_hour",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="weekplan",
            name="wed_research_self_study_min",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]