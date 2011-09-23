from social_auth.models import *
from app.tracker.models import *
import simplejson as json
import urllib, urllib2

def facebook_messages(user):
    FB_URL = 'https://graph.facebook.com/%s'
    url = FB_URL % ('me/inbox?access_token=%s&limit=10&offset=1' % user.extra_data['access_token'])
    message_list = json.loads(urllib2.urlopen(url).read())
    ca = ContactAccount.objects.filter(contact__in=(Contact.objects.filter(user=user.user)))
    ca_list = []
    for contact in ca:
        ca_list.append(contact.account_id)
    messages = []
    for message in message_list['data']:
        if message['from']['id'] in ca_list:
            interaction, created = Interaction.objects.get_or_create(\
                source=ContactAccount.objects.get(service=Service.objects.get(medium=5),\
                contact__in=Contact.objects.filter(user=user.user)), \
                content=message['message'], \
                #created_at=message['updated_time']
            )
            if created:
                interaction.save()
    return messages
    
def facebook_user(request, user):
    fb_user = UserSocialAuth.objects.get(user=request.user, provider='facebook')
    FB_URL = 'https://graph.facebook.com/%s'
    url = FB_URL % ('%s?access_token=%s' % (user, fb_user.extra_data['access_token']))
    user = json.loads(urllib2.urlopen(url).read())
    return user['name']

def load_data():
    for user in UserSocialAuth.objects.filter(provider='facebook'):
        facebook_messages(user)
        