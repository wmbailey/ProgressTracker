from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *

urlpatterns = patterns('tracker.views',
    url(r'^$', 'index', name='index'),
    url(r'^profile/contact/add.json', 'add_contact', name='add_contact'),
    url(r'^accounts/profile/', 'user_profile', name='user_profile'),
    url(r'^logout/$', 'user_logout', name='user_logout'),
)

