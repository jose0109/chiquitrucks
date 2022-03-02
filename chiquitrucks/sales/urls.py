from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.SaleListView.as_view(),name='sales_list'),
    path('new/',views.CreateSaleView.as_view(),name='sale_new'),
    path('<int:pk>/edit/',views.SaleUpdateView.as_view(),name='sale_edit'),
    path('<int:pk>/remove/',views.SaleDeleteView.as_view(),name='sale_remove'),
    path('payment-methods/',views.PmListView.as_view(),name='payment_methods'),
    path('payment-methods/new',views.PmCreateView.as_view(),name='pm_new'),
    path('payment-methods/<int:pk>/remove',views.PmDeleteView.as_view(),name='pm_remove'),
]
