# Generated by Django 2.0.1 on 2018-02-01 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20180202_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='organizator',
        ),
    ]
