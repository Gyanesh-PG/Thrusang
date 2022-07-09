from django.contrib import admin
from .models import profile,workshop,iplcount,thrusangtank,transactions
# Register your models here.
admin.site.register(profile)
admin.site.register(workshop)
admin.site.register(iplcount)
admin.site.register(thrusangtank)
admin.site.register(transactions)