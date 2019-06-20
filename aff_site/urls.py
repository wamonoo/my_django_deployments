from django.conf.urls import url
from django.urls import path
from aff_site import views
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from aff_site.api import ParticipantApi
#from django.views.generic import list_detail

#specify for URL Template tagging
app_name = 'aff_site'

urlpatterns = [
    url(r'^$',views.home, name = 'home'),
    url(r'^contacts/$',views.contacts, name = 'contacts'),
    url(r'^overview/$',views.overview, name ='overview' ),
    url(r'^login/$', views.user_login, name = 'user_login'),
    url(r'^logout/$', views.user_logout, name = 'user_logout'),
    url(r'^portal_landing/$', views.portal_landing, name = 'portal_landing'),
    url(r'^registration/$', views.register, name='register'),
    url(r'^signup/$', views.signup, name = 'signup'),
    #url(r'^users_report/$', views.users_report, name = 'users_report'),
    #use @api_view decorator in views
    #url(r'^participantlist/$', views.participantlist, name = 'participantlist'),
    #use with class based view
    #url(r'^participantlist/$', ParticipantApi.as_view()),
    url(r'^participant/$', views.participant_list, name = 'participant_list'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
