from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^team/$', views.team, name='team'),
    url(r'^services/$', views.services, name='services'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^events/$', views.events, name='events'),
    url(r'^insights/$', views.blog, name='blog'),
    url(r'^blog1/$', views.blog1, name='blog1'),
    url(r'^gurugram/$', views.gurugram, name='gurugram'),
    url(r'^contact/$', views.contact, name='contact'),
]
