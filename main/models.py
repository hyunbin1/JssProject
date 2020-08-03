from django.db import models

# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    update_at = models.DateTimeField(null=True, auto_now=True) 


# Primary key = pk = 데이터를 다룰때 사용하는 값 -  오브젝트를 식별할 수 있는 값 - 중복될 수 없는 단일 값






