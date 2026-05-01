"""
URL configuration for crm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from crm_app.views import index_view, campaigns_view, lead_view, promote_lead_view, customers_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="home"),
    path("products/", index_view, name="products"),
    path("ads/", campaigns_view, name="campaigns"),
    path("leads/", lead_view, name="leads"),
    path('leads/<int:lead_id>/promote/', promote_lead_view, name='create_contract'),
    path('customers/', customers_view, name='customers_list'),
]
