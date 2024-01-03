from django.db import models
import uuid

class NewsLetter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return str(self.email)
