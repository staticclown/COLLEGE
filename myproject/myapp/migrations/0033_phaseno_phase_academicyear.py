# Generated by Django 4.2.2 on 2023-06-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_phase_exp'),
    ]

    operations = [
        migrations.CreateModel(
            name='phaseno',
            fields=[
                ('no', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='phase',
            name='academicyear',
            field=models.CharField(default='2023', max_length=20),
        ),
    ]