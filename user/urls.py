from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.signup, name='user_register'),
    path('thank/', views.thankyou, name='thank'),
    path('signin/',views.signin, name='signin')
]