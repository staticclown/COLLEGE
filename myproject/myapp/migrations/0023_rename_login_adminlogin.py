# Generated by Django 4.2.1 on 2023-06-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0022_alter_teacher_pos"),
    ]

    operations = [
        migrations.RenameModel(old_name="Login", new_name="AdminLogin",),
    ]
