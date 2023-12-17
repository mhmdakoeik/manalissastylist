# Generated by Django 4.2.5 on 2023-12-16 12:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='uploads/homeGallery/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='uploads/homeGallery/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='uploads/homeGallery/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='uploads/homeGallery/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='uploads/homeGallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('main_title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/slider/')),
            ],
        ),
        migrations.CreateModel(
            name='WhyChooseOurServices',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='uploads/whyOurServices/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]