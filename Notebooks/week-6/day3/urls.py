"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from helloworld.views import index_view, football_view, dow_view, name_view, FootballView, StupidView

urlpatterns = [
    url(r"^$", index_view, name="index"),
    url(r"^stupid_view/", StupidView.as_view(), name="stupid_view"),
    url(r"^name_joiner/supercalafr/PYTHONRULES/$", name_view, name="joiner"),
    url(r'^football/', football_view, name="football"),
    url(r'^football_class/', FootballView.as_view(), name="football_cbv"),
    url(r'^dow/(?P<dow>\d{4}-\d{2}-\d{2})', dow_view, name="dow"),
    url(r'^admin/', include(admin.site.urls)),
]
