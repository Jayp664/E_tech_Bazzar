"""
URL configuration for E_tech_Bazzar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myadmin import views

urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('dash', views.dash, name='dash'),
    path('common_form', views.common_form, name='commn_form'),
    path('add_cat', views.add_categories, name='add_cat'),
    path('add_subcat', views.add_subcat, name='add_subcat'),
    path('common_table', views.common_table, name='common_table'),
    path('all_subcat', views.all_subcat, name='all_subcat'),
    path('all_cat', views.all_cat, name='all_cat'),
    path('view_customer', views.view_customer, name='view_customer'),
    path('view_order', views.view_order, name='view_order'),
    path('payment', views.payment, name='payment'),
    path('signin', views.signin, name='signin'),
]
