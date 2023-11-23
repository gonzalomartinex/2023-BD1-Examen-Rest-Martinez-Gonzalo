from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('categories/', views.categories),
    path('categories/<int:id>/', views.categoriesid),

    path('customers/', views.customers),
    path('customers/<str:id>/', views.customersid),

    path('suppliers/', views.suppliers),
    path('suppliers/<int:id>/', views.suppliersid),

    path('products/', views.products),
    path('products/<int:id>/', views.productsid),

    path('orders/', views.orders),
    path('orders/<int:id>/', views.ordersid),

    path('orderdetails/', views.orderdetails),
    path('orderdetails/<int:id>/', views.orderdetailsid),

    path('employees/', views.employees),
    path('employees/<int:id>/', views.employeesid),

    path('endpoint1/', views.endpoint1),

]
