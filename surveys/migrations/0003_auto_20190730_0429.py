# Generated by Django 2.2.3 on 2019-07-30 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userManagement.Department'),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('question_type', models.CharField(choices=[('radio', 'Radio'), ('short_answer', 'Short Answer'), ('long_answer', 'Long Answer'), ('number', 'Number')], max_length=32)),
                ('Section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=128)),
                ('value', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Question')),
            ],
        ),
    ]
