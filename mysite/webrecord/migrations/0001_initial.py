# Generated by Django 4.2.3 on 2024-09-25 03:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation time')),
                ('last_modify_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modify time')),
            ],
        ),
        migrations.CreateModel(
            name='AddrRecode',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webrecord.basemodel')),
                ('description', models.CharField(max_length=128, unique=True, verbose_name='descrption')),
                ('addr', models.URLField(unique=True, verbose_name='address')),
            ],
            bases=('webrecord.basemodel',),
        ),
    ]
