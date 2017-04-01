from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^home/$', views.home, name = 'home' ),
    url(r'^index/$', views.index, name = 'index' ),
    url(r'^topics/$', views.list_topics, name = 'list' )
]