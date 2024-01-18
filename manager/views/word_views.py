from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from ..models import WordTest
from check.models import StudentRegister
from ..forms import WordTestForm
from django.conf import settings
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def index(request):
    # students = StudentRegister.objects.filter(is_dropped=False)
    students_p = StudentRegister.objects.filter(class_name='P').order_by('class_num')
    students_s = StudentRegister.objects.filter(class_name='S').order_by('class_num')
    students_m = StudentRegister.objects.filter(class_name='M').order_by('class_num')

    p_line1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    p_line2 = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    s_line1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
               '18', '19', '20']
    s_line2 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
               '38', '39', '40']
    s_line3 = ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57',
               '58', '59', '60']

    context = {'students_p': students_p, 'students_s': students_s, 'students_m': students_m, 'p_line1': p_line1,
               'p_line2': p_line2, 's_line1': s_line1, 's_line2': s_line2, 's_line3': s_line3}

    return render(request, 'manager/word/word_main.html', context)

def word_detail(request):
    data = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')
    student = StudentRegister.objects.filter(id=student_id)  # 단일 객체를 가져오기
    # research3 = student.values('research3_select')[0]['research3_select']

    selected_week = request.GET.get('selected_week')

    if selected_week:
        filtered_data = Student_Study_Data.objects.filter(week_name=selected_week, user__id=student_id)
        total_study = filtered_data[0].korean_study + filtered_data[0].math_study + filtered_data[0].english_study + \
                      filtered_data[0].research1_study + filtered_data[0].research2_study
        total_self_study = filtered_data[0].korean_self_study + filtered_data[0].math_self_study + filtered_data[
            0].english_self_study + filtered_data[0].research1_self_study + filtered_data[0].research2_self_study
    else:
        filtered_data = []
        total_study = 0
        total_self_study = 0

    print(student)
    context = {
        'data': data,
        'student': student,
        'research1': research1,
        'research2': research2,
        'selected_week': selected_week,
        'filtered_data': filtered_data,
        'total_study': total_study,
        'total_self_study': total_self_study
    }
    return render(request, 'manager/student_study/student_study_detail.html', context)

def word_create(request, student_id):
    student = StudentRegister.objects.get(id=student_id)
    if request.method == 'POST':
        form = WordTestForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            return redirect('manager:word_detail', student_id)
    else:
        form = WordTestForm()
    context = {'form': form, 'student': student}
    return render(request, 'manager/word/word_form.html', context)

def word_modify(request, data_id):
    word_test = get_object_or_404(WordTest, pk=data_id)
    student = get_object_or_404(StudentRegister, id=word_test.user_id)
    student_id = student.id

    if request.method == "POST":
        form = WordTestForm(request.POST, instance=word_test)
        if form.is_valid():
            word_test = form.save(commit=False)
            word_test.save()
            return redirect('manager:word_detail', stu_id=question.id)
    else:
        form = WordTestForm(instance=word_test)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
def word_delete(request, data_id):