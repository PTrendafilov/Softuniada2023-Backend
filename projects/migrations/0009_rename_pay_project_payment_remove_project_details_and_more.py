# Generated by Django 4.1.3 on 2023-02-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='pay',
            new_name='payment',
        ),
        migrations.RemoveField(
            model_name='project',
            name='details',
        ),
        migrations.AddField(
            model_name='project',
            name='responsibilities',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.TextField(default=None),
        ),
    ]
