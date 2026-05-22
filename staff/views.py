from django.shortcuts import render, get_object_or_404
from .models import StaffMember


def leaders(request):
    leaders = StaffMember.objects.filter(role='leader', is_active=True)
    return render(request, 'staff/leaders.html', {'leaders': leaders})


def teachers(request):
    teachers = StaffMember.objects.filter(role='teacher', is_active=True)
    subjects = teachers.values_list('subject', flat=True).distinct()
    subject_filter = request.GET.get('subject')
    if subject_filter:
        teachers = teachers.filter(subject=subject_filter)
    subject_display = dict(StaffMember.SUBJECT_CHOICES)
    subjects_with_names = [(s, subject_display.get(s, s)) for s in subjects if s]
    return render(request, 'staff/teachers.html', {
        'teachers': teachers,
        'subjects': subjects_with_names,
        'selected_subject': subject_filter,
    })


def staff_detail(request, pk):
    member = get_object_or_404(StaffMember, pk=pk, is_active=True)
    return render(request, 'staff/detail.html', {'member': member})



