from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Project)