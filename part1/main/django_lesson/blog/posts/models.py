from django.db import models
from django.contrib.auth.models import User

# None = null
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
