# Generated by Django 4.2.2 on 2023-06-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_phaseno_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='classdivisions',
            name='sem',
            field=models.CharField(default='s1', max_length=20),
            preserve_default=False,
        ),
    ]
