# Generated by Django 2.2.6 on 2019-11-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0039_auto_20191030_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(null=True),
        ),
    ]
