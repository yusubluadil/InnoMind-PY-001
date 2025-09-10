from django.shortcuts import render
from django.http import HttpResponse

from .models import Post



def all_blogs(request):
    all_posts = Post.objects.all()

    context = {
        'posts': all_posts
    }

    return render(request, 'all-blogs.html', context)


def detail_blog(request, pk):
    blog = Post.objects.get(id=pk)

    context = {
        'post': blog
    }

    return render(request, 'detail-blogs.html', context)


def create_blog(request):
    return HttpResponse('Blog yaratmaq ucun olan sehife')
