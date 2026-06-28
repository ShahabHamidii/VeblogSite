from django.urls import path

from . import views
from .models import Post

app_name = 'blog'
urlpatterns = [
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('list/', views.post_list, name='post_list'),
    path('search/', views.search, name='post_search'),
    path('contactus/', views.ContactUsView.as_view(), name='contactus'),
    path('user/', views.ProfileList.as_view(), name='user_profile'),
    path('messages', views.MessageList.as_view(), name='messages_list'),
    path('messages/edit/<int:pk>', views.MessageUpdateView.as_view(), name='messages_edit'),
    path('messages/delete/<int:pk>', views.MessageDeleteView.as_view(), name='messages_delete'),
    path('like/<int:pk>', views.like, name='like'),

]
