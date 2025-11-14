from django.db import models

from users.models import CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='orders')
    products = models.ManyToManyField('products.Product', related_name='orders')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
