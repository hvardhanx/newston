"""newston URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    url(r'^$', 'newston.apps.services.views.front_page', name='front_page'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/' }, name='logout'),
    url(r'^signup/', CreateView.as_view(template_name='registration/signup.html', form_class=UserCreationForm, success_url='/'), name='signup'),
    url(r'^about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    url(r'^status/', 'newston.apps.core.views.status', name='status'),
    url(r'^cookies/', TemplateView.as_view(template_name='core/cookies.html'), name='cookies'),
    url(r'^privacy/', TemplateView.as_view(template_name='core/privacy.html'), name='privacy'),
    url(r'^terms/', TemplateView.as_view(template_name='core/terms.html'), name='terms'),
    url(r'^(?P<slug>[-_\w]+)/', include('newston.apps.services.urls', namespace='services')),
    url(r'^admin/', include(admin.site.urls)),
)
