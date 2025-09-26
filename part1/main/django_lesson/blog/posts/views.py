from django.shortcuts import (
    render,
    redirect
)

from .models import Post
from .forms import PostForm


def all_blogs(request):
    all_posts = Post.objects.order_by('-id')

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
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'create-blog.html', context={"form": form})
    else:
        user = request.user
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = user
            new_form.save()
            form.save_m2m()
            return redirect('all_blogs')
