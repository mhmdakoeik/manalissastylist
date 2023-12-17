# Generated by Django 4.2.5 on 2023-12-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whychooseourservices',
            old_name='icon',
            new_name='icon_1',
        ),
        migrations.RenameField(
            model_name='whychooseourservices',
            old_name='text',
            new_name='text_1',
        ),
        migrations.RenameField(
            model_name='whychooseourservices',
            old_name='title',
            new_name='text_2',
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='icon_2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/whyOurServices/'),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='icon_3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/whyOurServices/'),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='icon_4',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/whyOurServices/'),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='text_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='text_4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='title_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='title_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='title_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whychooseourservices',
            name='title_4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]