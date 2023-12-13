from django.contrib import admin
from .models import MultiImageModel, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(MultiImageModel)
class MultiImageModelAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Image)