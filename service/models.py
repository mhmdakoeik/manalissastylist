from django.db import models
import uuid


class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=True,blank=True,max_length=200)
    main_image = models.ImageField(null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)
    long_description = models.TextField(null=True,blank=True)
    image_1 = models.ImageField(null=True,blank=True)
    what_include = models.TextField(null=True,blank=True)
    image_2 = models.ImageField(null=True,blank=True)
    in_addition = models.TextField(null=True,blank=True)

    def what_include_lines(self):
        return filter(None, (line.strip() for line in (self.what_include or '').splitlines()))

    def in_addition_lines(self):
        return filter(None, (line.strip() for line in (self.in_addition or '').splitlines()))
    
    def __str__(self):
        return self.title