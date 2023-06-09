# Generated by Django 4.2.1 on 2023-06-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0013_alter_teacher_tmail"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="depid",
            field=models.ForeignKey(
                default="S0001",
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.department",
            ),
        ),
    ]