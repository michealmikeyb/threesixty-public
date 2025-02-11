# Generated by Django 2.2.6 on 2019-10-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0033_dimension_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaults',
            name='dimensions',
            field=models.TextField(default='[{"name": "Knowledge/Core Competency", "description": "intended to measure the leader\\u2019s perceived knowledge, background and preparation for the assignment.", "color": "#D63A71", "icon": "/media//icons/default_icons/icon-knowledge.png"}, {"name": "Relationships", "description": "Intended to measure the leader\\u2019s perceived ability to listen empathetically, communicate and relate with all constituents.", "color": "#ECA09C", "icon": "/media//icons/default_icons/icon-relationships.png"}, {"name": "Vision", "description": "To assess the leader\\u2019s strengths in setting a clear, inspiring and realistic direction for the school district.", "color": "#E0B81F", "icon": "/media//icons/default_icons/icon-vision.png"}, {"name": "Management", "description": "Assessing the leader\\u2019s abilities and attention to basic operational details of the school district.", "color": "#AEAEB0", "icon": "/media//icons/default_icons/icon-management.png"}, {"name": "Ethics/Standards", "description": "Intended to assess the leader\\u2019s perceived tendency to base decisions and actions on high ethical standards and principles.", "color": "#C49A6B ", "icon": "/media//icons/default_icons/icon-ethics.png"}, {"name": "Advocacy", "description": "Measures leaders efforts and inclination to advocate for the district to external audiences.", "color": "#AFCE5C", "icon": "/media//icons/default_icons/icon-advocacy.png"}, {"name": "Developer", "description": "Measuring the leaders inclination and efforts to develop and grow the strengths of others.", "color": "#DE6045", "icon": "/media//icons/default_icons/icon-developer.png"}, {"name": "Leadership Style", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Open Text", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Hogan HDS", "description": "Exploration of Hogan Derailers ", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Knowledge/Core Competency (MPS)", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Developer (MPS)", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Relator (MPS)", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Climate (MPS) ", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Standards (MPS)", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}, {"name": "Text Response (MPS)", "description": "", "color": "#8fc1ef", "icon": "/media//icons/default_icons/icon-default.png"}]', verbose_name='Dimensions'),
        ),
    ]
