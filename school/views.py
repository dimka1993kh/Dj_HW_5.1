from django.views.generic import ListView
from django.shortcuts import render
from .models import Teacher, Student
import random
from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    teachers = list(Teacher.objects.all())
    students = Student.objects.prefetch_related('teacher')
    added = Student.objects.first().teacher.first()
    if not added:
        for student in students:
            for i in range(random.randrange(1, len(teachers))):
                person = random.choice(teachers) 
                student.teacher.add(person)

    context = {
        'object_list': students,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
