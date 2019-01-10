from django.db import models

# Create your models here.

class Feed(models.Model):
    location = models.CharField(max_length=100)
    camera_link = models.CharField(max_length=1000)
    file_type = models.CharField(max_length=8)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.location
