from django.db import models
import uuid


class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=True,blank=True,max_length=200)
    main_image = models.ImageField(null=True,blank=True,upload_to='uploads/services/')
    short_description = models.TextField(null=True,blank=True)
    long_description = models.TextField(null=True,blank=True)
    image_1 = models.ImageField(null=True,blank=True,upload_to='uploads/services/')
    what_include = models.TextField(null=True,blank=True)
    priority = models.Integer(null=True,blank=False)
    
    def __str__(self):
        return str(self.title)

class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='uploads/avatar/',null=True,blank=True)
    name = models.CharField(blank=True,null=True,max_length=200)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField(null=True,blank=True)
    show = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return str(self.name)