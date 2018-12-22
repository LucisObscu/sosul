from django.db import models

# Create your models here.

class Sosul(models.Model):
    title = models.CharField(max_length=50)
    ko_title = models.CharField(max_length=50)
    update_count = models.IntegerField(max_length=10)
    data_path = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    keyword = models.CharField(max_length=20)
    date = models.DateTimeField()