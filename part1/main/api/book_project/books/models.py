from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    publishing_house_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2) # 9999.99
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='books', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)