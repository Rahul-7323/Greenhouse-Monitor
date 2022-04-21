from django.urls import re_path
from django_mongo_api import views

urlpatterns = [
    re_path(r'^api/test$', views.test_data),
    re_path(r'^api/sensor$', views.sensor_data),
]
