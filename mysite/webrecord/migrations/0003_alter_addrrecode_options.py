# Generated by Django 4.2.3 on 2024-10-29 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webrecord', '0002_alter_addrrecode_options_addrrecode_views_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addrrecode',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'get_latest_by': 'id', 'ordering': ['create_time', '-description']},
        ),
    ]
