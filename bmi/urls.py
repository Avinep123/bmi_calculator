# bmi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate/', views.calculate_bmi, name='calculate_bmi'),
    path('view/', views.view_data, name='view_data'),
    path('suggestions/<str:bmi_classification>/', views.suggestions, name='suggestions'),
]
