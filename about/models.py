from django.db import models
import uuid


class About(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,upload_to='uploads/about/')
    main_title = models.CharField(null=True,blank=True,max_length=200)
    main_top = models.CharField(null=True,blank=True,max_length=800)
    main_bottom = models.CharField(null=True,blank=True,max_length=800)
    paragraph_title_1 = models.CharField(null=True,blank=True,max_length=200)
    paragraph_1 = models.TextField(null=True,blank=True)                                                    
    paragraph_title_2 = models.CharField(null=True,blank=True,max_length=200)
    paragraph_2 = models.TextField(null=True,blank=True)                                                    
    paragraph_title_3 = models.CharField(null=True,blank=True,max_length=200)
    paragraph_3 = models.TextField(null=True,blank=True)                                                    
    paragraph_title_4 = models.CharField(null=True,blank=True,max_length=200)                          
    paragraph_4 = models.TextField(null=True,blank=True)                          
    
    
    def __str__(self):
        return self.main_title
