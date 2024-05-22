from django import views
from django.urls import path
from .import views



urlpatterns = [

    path('', views.index, name='index'),
    path('add/', views.add_tender, name='add_tender'),
    path('edit/<str:pk>/', views.edit_tender, name='edit_tender'),
    path('delete/<str:pk>/', views.delete_tender, name='delete_tender'),
    path('view/<str:pk>/', views.view_tender, name='view_tender'),


]