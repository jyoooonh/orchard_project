from django.urls import path

from .views import base_views, reserve_views, consulting_views, student_study_views, patrol_views, report_views, \
    data_views, teacher_views, word_views, weekplan_views

app_name = 'manager'

urlpatterns = [
    path('', base_views.index, name='index'),

    # reserve
    path('reserve/', reserve_views.reserve, name='reserve'),
    path('reserve/detail/<int:teacher_id>', reserve_views.reserve_detail, name='reserve_detail'),
    path('reserve/detail/<int:teacher_id>/<str:date>', reserve_views.reserve_detail_teacher,
         name='reserve_detail_teacher'),
    path('reserve/update/<int:reserve_id>/', reserve_views.reserve_update, name='reserve_update'),
    path('reserve/create/', reserve_views.reserve_create, name='reserve_create'),

    # teacher
    path('teacher/', teacher_views.teacher, name='teacher'),
    path('teacher_create/', teacher_views.teacher_create, name='teacher_create'),
    path('teacher_modify/<int:teacher_id>', teacher_views.teacher_modify, name='teacher_modify'),

    # student_study
    path('student_study/', student_study_views.new_student_study, name='student_study'),
    path('student_study/detail/<int:student_id>', student_study_views.new_student_study_detail, name='student_study_detail'),
    path('student_study/create/<int:student_id>', student_study_views.planner_create, name="planner_create"),
    path('student_study/modify/<int:data_id>', student_study_views.planner_modify, name="planner_modify"),
    path('student_study/delete/<int:data_id>', student_study_views.planner_delete, name="planner_delete"),

    path('student_study/upload/success', student_study_views.student_study_upload_success,
         name='student_study_upload_success'),
    path('student_study/upload/fail', student_study_views.student_study_upload_fail, name='student_study_upload_fail'),

    # weekplan
    path('weekplan/', weekplan_views.weekplan, name='weekplan'),
    path('weekplan/detail/<int:student_id>', weekplan_views.weekplan_detail, name='weekplan_detail'),
    path('weekplan/create/<int:student_id>', weekplan_views.weekplan_create, name='weekplan_create'),
    path('weekplan/modify/<int:data_id>', weekplan_views.weekplan_modify, name='weekplan_modify'),
    path('weekplan/delete/<int:data_id>', weekplan_views.weekplan_delete, name='weekplan_delete'),

    # word
    path('word/', word_views.index, name='word'),
    path('word/detail/<int:student_id>', word_views.word_detail, name='word_detail'),
    path('word/create/<int:student_id>', word_views.word_create, name='word_create'),
    path('word/modify/<int:data_id>', word_views.word_modify, name='word_modify'),
    path('word/delete/<int:data_id>', word_views.word_delete, name='word_delete'),

    # consulting
    path('consulting/', consulting_views.index, name='consulting'),
    path('consulting/detail/<int:student_id>', consulting_views.consulting_detail, name='consulting_detail'),
    path('consulting/create/<int:student_id>', consulting_views.consulting_create, name='consulting_create'),
    path('consulting/modify/<int:data_id>', consulting_views.consulting_modify, name='consulting_modify'),
    path('consulting/delete/<int:data_id>', consulting_views.consulting_delete, name='consulting_delete'),

    # patrol
    path('patrol/', patrol_views.patrol, name='patrol'),
    path('patrol/student_detail', patrol_views.patrol_student_detail, name='patrol_student_detail'),
    path('patrol/upload/success', patrol_views.patrol_upload_success, name='patrol_upload_success'),
    path('patrol/upload/fail/', patrol_views.patrol_upload_fail, name='patrol_upload_fail'),

    # data
    path('data/', data_views.index, name='data'),
    path('data/create/week/patrol/data/', data_views.create_week_patrol_data, name='create_week_patrol_data'),
    path('data/create/total/study/data/', data_views.create_total_study_data, name='create_total_study_data'),
    path('data/create/average/patrol/data/', data_views.create_average_patrol_data, name='create_average_patrol_data'),
    path('data/success/', data_views.patrol_weekly_data_success, name='patrol_weekly_data_success'),

    # report -> study
    path('report/study/', report_views.report_study_main, name='report_study_main'),
    path('report/study/detail/', report_views.report_study_detail, name='report_study_detail'),

    # report -> consulting
    path('report/consulting/', report_views.report_consulting_main, name='report_consulting_main'),
    path('report/consulting/detail', report_views.report_consulting_detail, name='report_consulting_detail')

    # report -> grade


]
