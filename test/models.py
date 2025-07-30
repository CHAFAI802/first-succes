from django.db import models

# Create your models here

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    summary = models.TextField()
    photo = models.ImageField(upload_to='speakers/%y%m%d')
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    biography_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


    