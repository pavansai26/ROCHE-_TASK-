from django.db import models

# Create your models here.
class FizzBuzzRequest(models.Model):
    int1 = models.IntegerField()
    int2 = models.IntegerField()
    limit = models.IntegerField()
    str1 = models.CharField(max_length=50)
    str2 = models.CharField(max_length=50)
    hits = models.IntegerField(default=0)