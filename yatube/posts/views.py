# posts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    title = 'Последние обновления на сайте'
    text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = f'Записи сообщества {group.title}'
    text = f'Записи сообщества {group.title}'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/group_list.html', context)

def show_base_template(request):
    template = 'base.html'
    return render(request, template)