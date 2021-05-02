from django.urls import path

from . import views


app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='list'),
    path('create', views.CreateGroup.as_view(), name='create'),
    path('delete', views.DeleteGroup.as_view(), name='delete'),
]