# Generated by Django 4.2.1 on 2023-06-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_alter_subject_depid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject", name="subname", field=models.CharField(max_length=25),
        ),
    ]
