from django.db import models
from cloudinary.models import CloudinaryField


class Articles(models.Model):
    
    name = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=10000)
    image = CloudinaryField('images')

    class Meta:
        verbose_name_plural = 'Articles'
    



