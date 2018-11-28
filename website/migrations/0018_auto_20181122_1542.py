# Generated by Django 2.0.6 on 2018-11-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_remove_management_old_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controller',
            name='power',
        ),
        migrations.AddField(
            model_name='network_devices',
            name='console_pass',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='network_devices',
            name='enable_pass',
            field=models.CharField(max_length=100, null=True),
        ),
    ]