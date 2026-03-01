from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Post,Adv


def home_page(request):
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')
    advs = Adv.objects.all()[:4]
    context = {
        'hot_posts': hot_posts,
        'posts': posts,
        'advs': advs
    }
    return render(request, 'index.html', context)


def all_news_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'all-news.html', {'posts': posts})


def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'news-by-category.html', context)


def search_page(request):
    return render(request, 'search.html')


def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, "search-results.html", {
        'results': results,
        'query': query
    })


def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'read-news.html', {'post': post})
