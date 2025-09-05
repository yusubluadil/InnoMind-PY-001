from django.db import models


class Announcement(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    release_year = models.IntegerField()
    engine_capacity = models.FloatField()
    mileage = models.IntegerField()
    city_name = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now_add=True)
