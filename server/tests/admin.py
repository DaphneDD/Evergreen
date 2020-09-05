from django.contrib import admin
from .models import Candidate, Test_Center, Client, Exam, Test

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Test_Center)
admin.site.register(Client)
admin.site.register(Exam)
admin.site.register(Test)