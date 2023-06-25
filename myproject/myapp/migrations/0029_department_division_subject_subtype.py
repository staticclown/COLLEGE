# Generated by Django 4.2.2 on 2023-06-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_classdivisions'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='division',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='subtype',
            field=models.CharField(default='T', max_length=5),
        ),
    ]