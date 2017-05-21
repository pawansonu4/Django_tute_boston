from django.conf.urls import url
from . import views

app_name='music'
urlpatterns = [

    #/music/
    url(r'^$', views.index, name='index'),

    #/music/albumid/
    url(r'^(?P<album_id>[0-9]+)/$', views.details,name='detail'),
    #/music/albumid/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite,name='favourite'),
]
