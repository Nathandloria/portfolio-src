# Generated by Django 3.1.3 on 2020-11-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='res',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
