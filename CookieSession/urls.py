from django.urls import path, re_path
from CookieSession import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('order/', views.order)
]