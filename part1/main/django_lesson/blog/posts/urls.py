from django.urls import path

from .views import (
    all_blogs,
    detail_blog,
    create_blog
)


# http://127.0.0.1:8000/posts/ - All blogs
# http://127.0.0.1:8000/posts/<id>/ - Detail blog
# http://127.0.0.1:8000/posts/create/ - Create blog

urlpatterns = [
    path('', all_blogs),
    path('<int:pk>/', detail_blog),
    path('create/', create_blog)
]
