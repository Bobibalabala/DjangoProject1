"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path
from .adminsite import admin_site

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# i18n_patterns： 支持国际化URL的函数 en/ zh/ 包含在url里以确定用什么语言
urlpatterns += i18n_patterns(re_path(r'^admin/', admin_site.urls),
                             re_path(r'', include('accounts.urls', namespace='accounts')),)