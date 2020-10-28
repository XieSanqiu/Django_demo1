'''
app01的路由分发
'''
from django.contrib import admin
from django.urls import path, re_path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('extend/', views.extend),
    path('staticTest/', views.static),
    path('search/', views.search),
    path('search-get/', views.search_get),
    path('search-post', views.search_post),
    re_path("index/([0-9]{4})/([0-9]{2})/$", views.index),
    re_path("^date/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.date),
    path('login/', views.login, name='reverse_login'),
]
