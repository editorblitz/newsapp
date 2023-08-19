"""
URL configuration for GrappelliProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', home, name='home'),  # Add this line
    path('grappelli/', include('grappelli.urls')),  # grappelli URLs
    path('admin/', admin.site.urls),  # admin site
    path('posts/', include('posts.urls')),
    path('dashboard/', include('dashboard.urls')),  # dashboard app URLs
]

admin.site.site_header = "News App admin"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)