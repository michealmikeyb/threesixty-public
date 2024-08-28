# Generated by Django 2.2.4 on 2019-09-09 09:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0017_auto_20190909_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='emails',
            field=models.TextField(default='', verbose_name='Emails'),
        ),
        migrations.CreateModel(
            name='ParticipantKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='key')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'ParticipantKey',
                'verbose_name_plural': 'ParticipantKeys',
            },
        ),
    ]
