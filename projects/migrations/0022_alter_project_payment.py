# Generated by Django 4.1.3 on 2023-02-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_project_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='payment',
            field=models.IntegerField(),
        ),
    ]
