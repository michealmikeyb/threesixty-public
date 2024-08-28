# Generated by Django 2.2.5 on 2019-10-15 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userManagement', '0009_auto_20190925_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='rid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'RegistrationRequest',
                'verbose_name_plural': 'RegistrationRequests',
            },
        ),
    ]
