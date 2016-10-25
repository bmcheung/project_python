from django.conf.urls import url

urlpatterns = [
    url(r'^', include('apps.login.urls', namespace = "login")),
    url(r'^home', include('apps.adoption.urls', namespace = "home")),
]
