from django.db.models import Q
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout, login, authenticate
from django.utils import simplejson
from django.core.context_processors import csrf
from social_auth.models import *
import urllib, urllib2
import operator
import sys
import simplejson as json

from django.conf import settings
from django import http
from django.template import Context, loader

def index(request):
    c = RequestContext(request, {})
    return render_to_response('login.html', c)

def facebook(request):
    c = RequestContext(request, {})
    return render_to_response('login.html', c)

def facebook_messages(user):
    fb_user = UserSocialAuth.objects.get(user=user, provider='facebook')
    FB_URL = 'https://graph.facebook.com/%s'
    url = FB_URL % ('me/inbox?access_token=%s&limit=11' % fb_user.extra_data['access_token'])
    likes = json.loads(urllib2.urlopen(url).read())
    print likes


def user_logout(request):
    logout(request)
    c = RequestContext(request, {})
    return render_to_response('login.html', c)

