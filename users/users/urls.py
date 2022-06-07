from django.urls import path
from users import views

urlpatterns=[
    path('users', views.login, name="login"),
    path('users/profile', views.profile, name='profile'),
    path('users/signup', views.signup, name='signup'),
    path('users/logout', views.logout, name='logout'),
]