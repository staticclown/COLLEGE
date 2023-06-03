from django.contrib import admin
from .models import Teacher,Subject,Department,Login

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Login)

# Register your models here.
