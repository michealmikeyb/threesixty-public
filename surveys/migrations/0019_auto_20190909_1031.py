# Generated by Django 2.2.4 on 2019-09-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0018_auto_20190909_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='admin_password',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='participant_password',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
