from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard-dashboard'),
    path('products/', views.products, name='dashboard-products' ),
]