# Generated by Django 4.1.3 on 2023-02-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_application_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]