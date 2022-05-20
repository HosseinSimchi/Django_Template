from django.contrib import admin
from django.urls import path,include
from MyApp.views import index_view

urlpatterns = [
    path('Home', index_view),
]
