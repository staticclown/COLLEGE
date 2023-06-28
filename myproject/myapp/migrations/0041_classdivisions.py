# Generated by Django 4.2.2 on 2023-06-28 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_delete_classdivisions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDivisions',
            fields=[
                ('classid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('classname', models.CharField(max_length=20)),
                ('classalloc', models.CharField(max_length=10)),
                ('exp', models.IntegerField()),
                ('sem', models.CharField(max_length=20)),
                ('subtype', models.CharField(max_length=20)),
                ('depid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.subject')),
            ],
        ),
    ]
