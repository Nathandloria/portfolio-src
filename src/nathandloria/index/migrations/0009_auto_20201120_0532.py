# Generated by Django 3.1.3 on 2020-11-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20201120_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='res',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
    ]