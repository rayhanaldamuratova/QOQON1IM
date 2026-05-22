from django.shortcuts import render, get_object_or_404
from .models import News, NewsCategory


def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-created_at')
    categories = NewsCategory.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        news = news.filter(category_id=category_id)
    return render(request, 'news/list.html', {
        'news': news,
        'categories': categories,
        'selected_category': category_id,
    })


def news_detail(request, pk):
    article = get_object_or_404(News, pk=pk, is_published=True)
    related = News.objects.filter(is_published=True).exclude(pk=pk).order_by('-created_at')[:3]
    return render(request, 'news/detail.html', {'article': article, 'related': related})



