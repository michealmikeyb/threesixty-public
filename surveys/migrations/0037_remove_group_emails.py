# Generated by Django 2.2.6 on 2019-10-28 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0036_auto_20191028_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='emails',
        ),
    ]
