# myapp/urls.py

from django.urls import path
from .views import register, user_login, user_logout,user_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
     path('user/',user_detail, name='user_detail'),
]
