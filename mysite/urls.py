"""mysite URL Configuration

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
from django.urls import path, include
from login import views
from captcha.views import captcha_refresh  # 验证码刷新功能，captcha_refresh为captcha.views内置方法，不需要我们单独写

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),  # 生成验证码
    path('refresh/', captcha_refresh),          # 点击可以刷新验证码
    path('confirm/', views.user_confirm),
]
