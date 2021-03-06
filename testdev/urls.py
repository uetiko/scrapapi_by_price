"""testdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from scrap.viewsets import ItemsAPI
from scrap.viewsets import ItemSKUAPI
from scrap.viewsets import ItemPriceAPI
from scrap.views import HomeView
from rest_framework_nested import routers


router = routers.DefaultRouter()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^items/$', ItemsAPI.as_view()),
    url(r'^items/(?P<sku>.+?)/$', ItemSKUAPI.as_view()),
    url(r'^item/price/(?P<price>\d+\.\d{2})/$', ItemPriceAPI.as_view())
]
