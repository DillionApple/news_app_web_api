from django.urls import path, include
from account import views

urlpatterns = [
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('register/', views.user_register),
    path('detail/', views.user_detail),
]
