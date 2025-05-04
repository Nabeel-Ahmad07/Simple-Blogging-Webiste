from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    img = models.ImageField(upload_to= 'pics', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
