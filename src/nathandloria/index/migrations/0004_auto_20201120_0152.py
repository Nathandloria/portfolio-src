# Generated by Django 3.1.3 on 2020-11-20 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20201120_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialicon',
            name='img_loc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='socialicon',
            name='link',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='socialicon',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
