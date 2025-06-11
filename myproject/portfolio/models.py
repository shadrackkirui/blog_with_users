from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
