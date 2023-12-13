from django.db import models
import uuid



class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

