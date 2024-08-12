"""
URL configuration for the myapp application.

This module maps URLs to views, including the integration
with the FastAPI application through the `fastapi_view`.
"""

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/(?P<path>.*)$', views.fastapi_view, name='fastapi_view'),
]
