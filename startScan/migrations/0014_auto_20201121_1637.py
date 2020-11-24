# Generated by Django 3.0.7 on 2020-11-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0013_vulnerabilityscan_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerabilityscan',
            name='status',
        ),
        migrations.AddField(
            model_name='vulnerabilityscan',
            name='open_status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]