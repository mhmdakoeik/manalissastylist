# Generated by Django 4.2.5 on 2023-12-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='show',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]