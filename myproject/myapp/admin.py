from django.contrib import admin
from .models import Teacher,Subject,Department,AdminLogin,TeacherLogin,TeacherSelection,ClassDivisions

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(AdminLogin)
admin.site.register(TeacherLogin)
admin.site.register(TeacherSelection)
admin.site.register(ClassDivisions)
# Register your models here.
