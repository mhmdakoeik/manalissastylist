from django.db import models
import uuid
class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='uploads/blog/')
    pargraph = models.TextField(null=True,blank=True)
    auth_name = models.TextField(null = True , blank=True)
    auth_image = models.ImageField(upload_to='uploads/blog/')
    
    def __str__(self):
        return self.title
