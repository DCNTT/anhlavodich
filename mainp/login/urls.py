from django.urls import path
from .import views

urlpatterns = [
    path('',views.Login.as_view(), name = 'Login' ),
    path('home/', views.Home, name = 'home'),
    path('test', views.test, name = 'test'),
]


