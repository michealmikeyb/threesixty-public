# Generated by Django 2.2.4 on 2019-09-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0013_survey_survey_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='template',
            field=models.BooleanField(default=False, verbose_name='Template'),
        ),
    ]
