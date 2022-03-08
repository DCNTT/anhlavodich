from django.urls import path
from .import views

urlpatterns =[
    path('', views.login, name='login'),
    path('reg/', views.reg, name = 'reg'),
    path('shift/', views.shift, name = 'shift'),
    path('add/', views.add, name = 'add'),
]