# Generated by Django 2.0.6 on 2018-11-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20181025_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='desc',
        ),
        migrations.AddField(
            model_name='management',
            name='new_config',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='management',
            name='old_config',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]