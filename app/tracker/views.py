from django.db.models import Q
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout, login, authenticate
from django.utils import simplejson
from django.core.context_processors import csrf
from django.contrib.messages.api import get_messages
from social_auth.models import *
from app.tracker.models import *
from app.tracker.utils import *
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

def user_profile(request):
    c = RequestContext(request, {})
    try:
        fb_user = UserSocialAuth.objects.get(user=request.user, provider='facebook')
        FB_URL = 'https://graph.facebook.com/%s'
        url = FB_URL % ('me/friends?access_token=%s' % fb_user.extra_data['access_token'])
        friends = json.loads(urllib2.urlopen(url).read())
        c['friends'] = friends
        c['messages'] = facebook_messages(request.user)
    except:
        print "Unexpected error:", sys.exc_info()
        pass
    return render_to_response('profile.html', c)

def add_contact(request):
    contact = Contact(name=facebook_user(request, request.REQUEST['userid']))
    contact.save()
    service = Service.objects.get(medium=5)
    ca = ContactAccount(contact=contact,service=service, account_id=request.REQUEST['userid'])
    ca.save()
    return HttpResponse(simplejson.dumps({'success':'true'}))

def login_error(request):
    c = RequestContext(request, {})
    for msg in get_messages(request):
        print msg.message
    return render_to_response('login.html',c)

def user_logout(request):
    logout(request)
    c = RequestContext(request, {})
    return render_to_response('login.html', c)


