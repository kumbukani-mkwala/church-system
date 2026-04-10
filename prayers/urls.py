from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_prayer, name='submit_prayer'),
    path('view/', views.view_prayers, name='view_prayers'),
]