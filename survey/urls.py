"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from master import urls as masterurls
from web import urls as weburls
from django.conf import settings
from django.conf.urls.static import static
from . import views
from api import urls as apiurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/',include(masterurls)),
    path('web/',include(weburls)),
    path('',views.index),
    path('api/',include(apiurls)),
]
