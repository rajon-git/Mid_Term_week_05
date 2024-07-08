
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/password_change', views.change_password, name='change_password'),
]
