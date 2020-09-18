from django.urls import path
from tomaggeul import views

urlpatterns = [
    path('main/', views.tmtext, name='main'),
]