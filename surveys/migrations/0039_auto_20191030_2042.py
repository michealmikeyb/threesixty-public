# Generated by Django 2.2.6 on 2019-10-30 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0038_group_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='emails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.EmailList', verbose_name='Emails'),
        ),
    ]
