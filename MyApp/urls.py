from django.contrib import admin
from django.urls import path,include
from MyApp.views import index_view
app_name = 'MyApp';

urlpatterns = [
    path('', index_view, name = "index"),
]
