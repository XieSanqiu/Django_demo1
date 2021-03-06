"""Django_demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from Django_demo1 import views
from AuthTest import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include(('app01.urls', 'app01'))), #加上名称空间 app01
    path('hello/', views.hello_world),
    path('login/', views.login, name='reverse_login'),
    re_path('login2/([0-9]{4})/$', views.login2, name='reverse_login2'),
    re_path('login3/(?P<year>[0-9]{4})/$', views.login3, name='reverse_login3'),
    path('model/', include('TestModel.urls')),
    path('add_emp/', views.add_emp),
    path('add_emp2/', views.add_emp2),
    path('AuthTest/', include('AuthTest.urls')),
    path('accounts/login/', auth_views.auth_login),
    path('CookieSession/', include(('CookieSession.urls', 'CookieSession'))),
]
