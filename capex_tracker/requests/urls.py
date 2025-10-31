from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('submit/', views.submit_request, name='submit_request'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('register/', views.register, name='register'),
]