# Generated by Django 3.1.5 on 2021-01-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
