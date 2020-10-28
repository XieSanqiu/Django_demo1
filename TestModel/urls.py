'''
TestModel的路由分发
'''
from django.contrib import admin
from django.urls import path, re_path
from TestModel import views
urlpatterns = [
    path('add/', views.test_db_add),
    path('query/', views.test_db_query),
    path('update/', views.test_db_update),
    path('delete/', views.test_db_delete),
]