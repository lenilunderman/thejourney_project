from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=60)
    project_short_description = models.CharField(max_length=120)
    project_description = models.TextField(blank=True)
    project_type = models.CharField(max_length=30,blank=True)
    project_image = models.ImageField(upload_to='projects/images/')
    project_url = models.URLField(blank=True)
    project_favorite = models.BooleanField(null=True)
    project_date = models.DateField()

    def __str__(self):
        return self.project_short_description
