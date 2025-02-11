# Generated by Django 2.2.5 on 2019-10-15 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0031_survey_email_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='free_use',
            field=models.BooleanField(null=True, verbose_name='Free Use'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('radio', 'Likert'), ('number', 'Number'), ('short_answer', 'Short Answer'), ('long_answer', 'Long Answer')], max_length=32),
        ),
    ]
