from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
     

    path('pastor/', views.pastor_dashboard, name='pastor_dashboard'),
    path('treasurer/', views.treasurer_dashboard, name='treasurer_dashboard'),
    path('secretary/', views.secretary_dashboard, name='secretary_dashboard'),
    path('member/', views.member_dashboard, name='member_dashboard'),
]