from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Rgform(User):
    num=models.IntegerField()
    img=models.ImageField(upload_to="gallery")
class RegistForm(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    num=models.IntegerField()
    img=models.ImageField(upload_to="gallery")
class RForm(User):
    Profile_photo=models.ImageField(upload_to='gallery')
    number=models.IntegerField(default='Null')