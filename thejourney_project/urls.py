from django.contrib import admin
from django.urls import path
# to create the folder for the images and static files
from django.conf.urls.static import static
from django.conf import settings
# to use other apps in the main project, necessary to import first and then use the views
from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
