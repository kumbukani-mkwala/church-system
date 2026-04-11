from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join_department, name='join_department'),
    path('member/', views.member_dashboard, name='member_dashboard'),

    path('approve/<int:membership_id>/', views.approve_membership, name='approve_membership'),

    path('praise/chat/', views.praise_chat, name='praise_chat'),
    path('media/chat/', views.media_chat, name='media_chat'),
    path('evangelism/chat/', views.evangelism_chat, name='evangelism_chat'),
]