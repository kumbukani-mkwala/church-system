from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join_department, name='join_department'),

    path("praise/chat/", views.praise_chat, name="praise_chat"),
    path("media/chat/", views.media_chat, name="media_chat"),
    path("evangelism/chat/", views.evangelism_chat, name="evangelism_chat"),
]