from django.db import models

class MultiImageModel(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.name if self.name else 'Unnamed MultiImageModel'


class Image(models.Model):
    multi_image = models.ForeignKey(MultiImageModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/gallery/')

    def __str__(self):
        return self.image.name
