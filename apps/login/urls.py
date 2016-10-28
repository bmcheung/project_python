from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^main/$', views.main, name= 'main'),
    url(r'^register/$', views.register, name= 'register'),
    url(r'^process/$', views.process, name = 'process'),
    url(r'^map/$', views.map, name = 'map'),
    url(r'^adopt/$', views.adopt, name = 'adopt'),
    url(r'^lost/$', views.lost, name = 'lost'),
    url(r'^lost/process$', views.lost_process, name = 'lost_process'),
    url(r'^found/$', views.found, name = 'found'),
    url(r'^found/process$', views.found_process, name = 'found_process')
]
