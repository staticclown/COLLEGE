from django.contrib import admin
from .models import Teacher,Subject,Department,AdminLogin,TeacherLogin,phaseget
from .models import phaseno,ClassDivisions,Phase,TeacherSelection,Final,semtype
from .models import Phaseteacher,clash

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(AdminLogin)
admin.site.register(TeacherLogin)
admin.site.register(TeacherSelection)
admin.site.register(ClassDivisions)
admin.site.register(Phase)
admin.site.register(phaseno)
admin.site.register(Final)
admin.site.register(semtype)
admin.site.register(phaseget)
admin.site.register(Phaseteacher)
admin.site.register(clash)
# Register your models here.
