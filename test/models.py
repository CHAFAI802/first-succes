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


class Session(models.Model):
    session_type = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    attendees = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.session_type})"


class SpeakerDetails(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='speakers/%Y/%m/%d')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    years_experience = models.CharField(max_length=50)
    sessions_count = models.PositiveIntegerField()
    companies_advised = models.CharField(max_length=200)
    quote = models.TextField()
    biography = models.TextField()
    expertise_areas = models.TextField(null=True)  # liste séparée par virgules
    sessions = models.ManyToManyField(Session)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    def get_expertise_list(self):
        return [area.strip() for area in self.expertise_areas.split(',') if area.strip()]

    def __str__(self):
        return self.full_name
  