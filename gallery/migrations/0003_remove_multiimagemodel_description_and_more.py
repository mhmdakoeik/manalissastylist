# Generated by Django 4.2.5 on 2023-12-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiimagemodel',
            name='description',
        ),
        migrations.AddField(
            model_name='multiimagemodel',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='uploads/gallery/'),
        ),
    ]
