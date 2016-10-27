from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^main/$', views.main, name= 'main'),
    url(r'^process/$', views.process, name = 'process'),
    url(r'^map/$', views.map, name = 'map'),
    url(r'^adopt/$', views.adopt, name = 'adopt')
]
