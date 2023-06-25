import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex = models.CharField("Sex",max_length=20)
    birth_date = models.DateField("Birth Date",default=datetime.date.today)
    is_online = models.BooleanField("Is Online", default = False)

class Links(models.Model):
    original_link = models.CharField("Original Link",max_length=255)
    short_link = models.CharField("Short Link",max_length=255, unique= True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True);
