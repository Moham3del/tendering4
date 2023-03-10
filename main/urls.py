from django.urls import path
from . import views


urlpatterns = [
    path('', views.userLogin, name='login'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    
    path('login_ar', views.userLogin_ar, name='login_ar'),
    path('register/', views.register, name='register'),
    path('register_ar/', views.register_ar, name='register_ar'),
    path('logout/', views.userLogout, name='logout'),
    path('user/', views.userProfile, name='user_profile'),
]