"""dabada_scholarship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('manager/', include('manager.urls')),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
    path('register/', views.register, name='register'),
    path('service1/', views.service1, name='service1'),
    path('service2/', views.service2, name='service2'),
    path('service3/', views.service3, name='service3'),
    path('service4/', views.service4, name='service4'),
    path('need_login/', views.need_login, name='need_login'),
    path('is_admin/', views.is_admin, name='is_admin'),
    #url pattern 앞에 index/ 이거 붙는 애들 처리해줘야함
    #url regular regex check
]
