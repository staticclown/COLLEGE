from django.contrib import admin
from .models import Teacher,Subject,Department,AdminLogin,TeacherLogin
from .models import TeacherSelection,phaseno,ClassDivisions,Phase

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(AdminLogin)
admin.site.register(TeacherLogin)
admin.site.register(TeacherSelection)
admin.site.register(ClassDivisions)
admin.site.register(Phase)
admin.site.register(phaseno)
# Register your models here.
