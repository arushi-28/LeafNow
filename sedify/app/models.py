from django.db import models
from django.forms import ModelForm
# Create your models here.
class donation(models.Model):
    amount=models.IntegerField()
    email=models.EmailField(max_length=20)
    nick=models.CharField(max_length=20)
    card=models.IntegerField(max_length=12)
class Meta:
    db_table="donation"