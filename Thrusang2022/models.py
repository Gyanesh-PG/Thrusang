from django.db import models
from django.contrib.auth.models import User
class profile(models.Model):
    id_no = models.CharField(max_length=20)
    college_name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    year_of_study = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    payment = models.CharField(max_length=10)
    pay_id = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
