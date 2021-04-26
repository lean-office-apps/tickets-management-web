from django.contrib.auth.views import LogoutView
from django.urls import path, re_path

from .views import login_view, register_user
from . import views


urlpatterns = [
    # TODO: move these urls to another app (Where? tbd)
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('', views.index, name='home'),  # The home page
    re_path(r'^.*\.*', views.pages, name='pages'),  # Matches any html file
]