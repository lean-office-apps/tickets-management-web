from django.urls import path

from . import views


app_name = 'tickets'

urlpatterns = [
    path('list/', views.TicketsListView.as_view(), name='list'),
    path('create/', views.TicketCreateView.as_view(), name='create'),
    path('<int:pk>/', views.TicketDetailView.as_view(), name='detail'),
]
