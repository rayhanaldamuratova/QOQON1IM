from django.shortcuts import render
from .models import SchoolInfo
from news.models import News
from achievements.models import Achievement


def home(request):
    school = SchoolInfo.objects.first()
    latest_news = News.objects.filter(is_published=True).order_by('-created_at')[:3]
    top_achievements = Achievement.objects.filter(is_published=True).order_by('-date')[:4]
    return render(request, 'core/home.html', {
        'school': school,
        'latest_news': latest_news,
        'top_achievements': top_achievements,
    })


def about(request):
    school = SchoolInfo.objects.first()
    return render(request, 'core/about.html', {'school': school})


def handler404(request, exception):
    return render(request, '404.html', status=404)



