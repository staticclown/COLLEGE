# Generated by Django 4.2.1 on 2023-06-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0023_rename_login_adminlogin"),
    ]

    operations = [
        migrations.RemoveField(model_name="adminlogin", name="id",),
        migrations.AlterField(
            model_name="adminlogin",
            name="pid",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]