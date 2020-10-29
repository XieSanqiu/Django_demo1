'''
auth模块的路由分发
'''
from django.urls import path, re_path
from AuthTest import views

urlpatterns = [
    path('create_user/', views.create_user),
    path('auth_login/', views.auth_login),
    path('auth_logout/', views.auth_logout),
    path('login_required/', views.login_required),
]