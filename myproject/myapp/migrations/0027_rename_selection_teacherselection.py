# Generated by Django 4.2.1 on 2023-06-22 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0026_teacherlogin_selection"),
    ]

    operations = [
        migrations.RenameModel(old_name="selection", new_name="TeacherSelection",),
    ]
