from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/(?P<path>.*)$', views.fastapi_view, name='fastapi_view'),
]
