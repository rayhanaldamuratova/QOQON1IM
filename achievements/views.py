from django.shortcuts import render
from .models import Achievement


def achievements_list(request):
    achievements = Achievement.objects.filter(is_published=True)
    category = request.GET.get('category')
    level = request.GET.get('level')
    if category:
        achievements = achievements.filter(category=category)
    if level:
        achievements = achievements.filter(level=level)
    return render(request, 'achievements/list.html', {
        'achievements': achievements,
        'categories': Achievement.CATEGORY_CHOICES,
        'levels': Achievement.LEVEL_CHOICES,
        'selected_category': category,
        'selected_level': level,
    })



