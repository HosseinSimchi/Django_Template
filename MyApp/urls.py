from django.contrib import admin
from django.urls import path,include
from MyApp.views import index_view,innerpage_view,PortFolio_view

urlpatterns = [
    path('', index_view, name = "index"),
    path('Page1', innerpage_view, name = "InnerPage"),
    path('Page2', PortFolio_view, name = "PortfolioDetails")
]
