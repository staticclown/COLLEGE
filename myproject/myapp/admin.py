from django.contrib import admin
from .models import Teacher,Subject,Department

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)

# Register your models here.
