from django.urls import path
from . import views


urlpatterns = [
    path('', views.googleSearch, name='index'),
]