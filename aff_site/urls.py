from django.conf.urls import url
from django.urls import path
from aff_site import views
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.views.generic import list_detail

#specify for URL Template tagging
app_name = 'aff_site'

urlpatterns = [
    url(r'^$',views.home, name = 'home'),
    url(r'^contacts/$',views.contacts, name = 'contacts'),
    url(r'^overview/$',views.overview, name ='overview' ),
    #url(r'^events/$', views.events, name = 'events'),
    #url(r'^registration/$', views.register.as_view(), name = 'register'),
    url(r'^registration/$', views.register, name='register'),
]
