from django.db import models
from django.contrib.auth.models import User

# None = null
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    image = models.ImageField(upload_to='posts', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title
