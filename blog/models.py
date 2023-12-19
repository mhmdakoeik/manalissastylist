from django.db import models
import uuid
class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    title = models.CharField(max_length=200,blank=False,null=False)
    content = models.TextField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
=======
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True,required=True)
    date = models.DateField(null=True,blank=True,required=True)
>>>>>>> 8d81ed29b5bc5bdd8467e3016b4b229ffa486f53
    image = models.ImageField(null=True,blank=True,upload_to='uploads/blog/',required=True)
    pargraph = models.TextField(null=True,blank=True)
    auth_name = models.TextField(null = True , blank=True)
    auth_image = models.ImageField(upload_to='uploads/blog/',required=False)
    
    def __str__(self):
        return str(self.title)
