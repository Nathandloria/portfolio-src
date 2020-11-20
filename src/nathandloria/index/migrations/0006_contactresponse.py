# Generated by Django 3.1.3 on 2020-11-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', models.CharField(default='', max_length=10000)),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('date', models.DateTimeField(default=None)),
            ],
        ),
    ]
