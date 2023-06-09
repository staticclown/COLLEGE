# Generated by Django 4.2.2 on 2023-07-06 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_delete_teacherselection'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherSelection',
            fields=[
                ('sub1', models.CharField(max_length=20)),
                ('sub2', models.CharField(max_length=20)),
                ('sub3', models.CharField(max_length=20)),
                ('sub4', models.CharField(max_length=20)),
                ('sub5', models.CharField(max_length=20)),
                ('sub6', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('selectionid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=20)),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher')),
            ],
        ),
    ]
