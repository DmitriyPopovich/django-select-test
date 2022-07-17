from django.urls import path, re_path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<brand>/', views.index, name='index'),
    path('<brand>/<service>/', views.index, name='index'),
    path('<brand>/<style>/', views.index, name='index'),
    path('<style>/', views.index, name='index'),
    path('<style>/<service>/', views.index, name='index'),
    path('<service>/', views.index, name='index'),
    path('<service>/<style>/', views.index, name='index'),
    path('<brand>/<service>/<style>/', views.index, name='index'),
]

