from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login", views.my_login, name='login'),
    path("logout", views.my_logout, name='logout'),
    path("signup", views.signup, name='signup', ),
    path("edit", views.edit_profile, name='edit'),
]
