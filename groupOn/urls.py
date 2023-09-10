from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home,  name="home"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("create_group/", views.create_group, name="logout"),
]
