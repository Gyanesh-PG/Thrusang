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
    ttpay = models.CharField(max_length=10)
    ttpay_id = models.CharField(max_length=100)
    iplpay = models.CharField(max_length=10)
    iplpay_id = models.CharField(max_length=100)
    pay_id = models.CharField(max_length=200)
    evpay = models.CharField(max_length=10)
    evpay_id = models.CharField(max_length=200)
    tt = models.CharField(max_length=10)
    sl = models.CharField(max_length=10)
    sb = models.CharField(max_length=10)
    tet = models.CharField(max_length=10)
    tc = models.CharField(max_length=10)
    deb = models.CharField(max_length=10)
    saw = models.CharField(max_length=10)
    cg = models.CharField(max_length=10)
    ipl = models.CharField(max_length=10)
    quiz = models.CharField(max_length=10)
    mp = models.CharField(max_length=10)
    ld = models.CharField(max_length=10)
    wb = models.CharField(max_length=10)
    sg = models.CharField(max_length=10)
    rd = models.CharField(max_length=10)
    bgmi = models.CharField(max_length=10)
    reg_time = models.CharField(max_length=100)
    evcount = models.IntegerField()
    ipcount = models.IntegerField()
    th_id = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class workshop(models.Model):
    name = models.CharField(max_length=80)
    payment = models.CharField(max_length=10)
    pay_id = models.CharField(max_length=200)
    tg=models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class iplcount(models.Model):
    name=models.CharField(max_length=20)
    count = models.PositiveSmallIntegerField(default=0)
class thrusangtank(models.Model):
    name=models.CharField(max_length=40)
    mobile=models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class transactions(models.Model):
    tans_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    trans_time = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)