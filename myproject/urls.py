"""
Django URL configuration.

This module defines the URL patterns for the Django project,
including the integration with FastAPI views.
"""

from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/<path:path>/', views.fastapi_view, name='fastapi_view'),
]
