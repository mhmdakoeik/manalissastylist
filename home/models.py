from django.db import models
import uuid

class Slider(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    main_title = models.CharField(null=True,blank=True,max_length=200)
    subtitle = models.CharField(null=True,blank=True,max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to='uploads/slider/')

    def __str__(self):
        return str(self.created)

class WhyChooseOurServices(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    icon_1 = models.ImageField(null=True,blank=True,upload_to='uploads/whyOurServices/')
    title_1 = models.CharField(null=True,blank=True,max_length=200)
    text_1 = models.CharField(null=True,blank=True,max_length=200)
    icon_2 = models.ImageField(null=True,blank=True,upload_to='uploads/whyOurServices/')
    title_2 = models.CharField(null=True,blank=True,max_length=200)
    text_2 = models.CharField(null=True,blank=True,max_length=200)
    icon_3 = models.ImageField(null=True,blank=True,upload_to='uploads/whyOurServices/')
    title_3 = models.CharField(null=True,blank=True,max_length=200)
    text_3 = models.CharField(null=True,blank=True,max_length=200)
    icon_4 = models.ImageField(null=True,blank=True,upload_to='uploads/whyOurServices/')
    title_4 = models.CharField(null=True,blank=True,max_length=200)
    text_4 = models.CharField(null=True,blank=True,max_length=200)

    def __str__(self):
        return str(self.created)

class Gallery(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    image_1 = models.ImageField(null=True,blank=True,upload_to='uploads/homeGallery/')
    image_2 = models.ImageField(null=True,blank=True,upload_to='uploads/homeGallery/')
    image_3 = models.ImageField(null=True,blank=True,upload_to='uploads/homeGallery/')


    def __str__(self):
        return str(self.created)
