from django.contrib import admin
# Import the model to be used in the admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    # custom columns
    list_display = ['project_title','project_short_description','project_short_description','project_date']

admin.site.register(Project,ProjectAdmin)