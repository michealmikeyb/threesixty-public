# Generated by Django 2.2.5 on 2019-09-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0008_auto_20190912_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headersettings',
            name='background',
            field=models.CharField(default='#000000', max_length=8, verbose_name='Background Color'),
        ),
        migrations.AlterField(
            model_name='headersettings',
            name='color',
            field=models.CharField(default='#C2EFF0', max_length=8, verbose_name='Text Color'),
        ),
    ]
