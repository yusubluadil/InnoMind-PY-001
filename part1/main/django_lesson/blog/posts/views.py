from django.shortcuts import (
    render,
    redirect
)
from django.db.models import Q

from .models import Post
from .forms import PostForm


def all_blogs(request):
    all_posts = Post.objects.order_by('-id')

    context = {
        'posts': all_posts
    }

    return render(request, 'blogs/all-blogs.html', context)


def detail_blog(request, pk):
    blog = Post.objects.get(id=pk)

    context = {
        'post': blog
    }

    return render(request, 'blogs/detail-blogs.html', context)


def create_blog(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogs/create-blog.html', context={"form": form})
    else:
        user = request.user
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = user
            new_form.save()
            form.save_m2m()
            return redirect('all_blogs')


def search_blog(request):
    q = request.GET['q']
    searched_data = Post.objects.filter(
        Q(title__icontains=q) |
        Q(author__username__icontains=q) |
        Q(author__first_name__icontains=q)
    )

    context = {
        'posts': searched_data
    }
    return render(request, 'blogs/all-blogs.html', context)
