from django.contrib import admin
from django.urls import path

# we need to import views from our information app
from information import views

urlpatterns = [
  path('', views.index, name='index'),
  path('submit/', views.Submit, name='Submit')
]