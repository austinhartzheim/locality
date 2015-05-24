from django.conf.urls import patterns, url
import api.views

urlpatterns = patterns('api.views',
    url(r'find_nearby/(?P<lat>[-0-9\\.]+),(?P<lng>[-0-9\\.]+)/', 'find_nearby')
)
