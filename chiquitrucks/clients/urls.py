from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.ClientListView.as_view(),name='client_list'),
    path('new/',views.CreateClientView.as_view(),name='client_new'),
    path('<int:pk>/edit/',views.ClientUpdateView.as_view(),name='client_edit'),
    path('<int:pk>/remove/',views.ClientDeleteView.as_view(),name='client_remove'),
]


