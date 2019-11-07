from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

#from djano.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout

#use REST framework with function based views
from rest_framework.decorators import api_view

from .forms import NewParticipant, SignupForm

#imports for populating django tables
from aff_site.models import Participant
from .tables import ParticipantTable
from django_tables2 import RequestConfig


def home(request):
    return render (request, 'aff_site/main_page.html')

def contacts(request):
    return render (request, 'aff_site/contacts.html')

def overview(request):
    return render (request, 'aff_site/overview.html')

def products(request):
    return render (request, 'aff_site/products.html')

def services(request):
    return render (request, 'aff_site/services.html')

def investors(request):
    return render (request, 'aff_site/investors.html')

def participant_list(request):
    table = ParticipantTable(Participant.objects.all())

    return render(request, 'participant_list.html', {
    'table': table
    })

#def registered_list(request):
#    return render (request, 'aff_site/registered_list.html')
#@api_view()
#def participantlist(request):
#    return render (request, 'aff_site/users_report.html')

@login_required
def portal_landing(request):
    return render (request, 'aff_site/portal_landing.html')

def user_login(request):

    if request.method == 'POST':
        #portal_user = Portal_user(request.POST or None)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('aff_site:portal_landing'))

            else:
                return HttpResponse ("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse ("Login failed")
    else:
        return render(request, 'aff_site/user_login.html', {})

#use decorator to make sure that only a user logged in can have logout option
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('aff_site:home'))


def signup(request):
    portal_user = False
    if request.method == 'POST':
        PortaluserForm = SignupForm(request.POST)
#extras from here
        if PortaluserForm.is_valid(): #and address_form.is_valid() and city_form.is_valid() and country_form.is_valid():

            user = PortaluserForm.save(commit = False)
            user.is_active = False
            user.save()

            portal_user = True

            #return HttpResponse('Thanks for registering as a user. Kindly log in to the platform within the next 12 hrs')
            '''
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = PortaluserForm.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')'''
    else:
        PortaluserForm = SignupForm()
    #return render(request, 'signup.html', {'PortaluserForm': PortaluserForm})
    return render (request, 'aff_site/signup.html',
                                    {'PortaluserForm':PortaluserForm,
                                    'portal_user':portal_user})

            #hash the password
            #user.set_password(user.password)

            #user.save()

            #PortaluserForm.save()


            #return HttpResponseRedirect(reverse('aff_site:home'))
    #else:
    #    PortaluserForm = SignupForm()
    #return render (request, 'create_portal_user.html',
    #                            {'PortaluserForm':PortaluserForm})


#activate function
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def register(request):

    registered = False

    if request.method == "POST":
        participant_form = NewParticipant(request.POST)
#extras from here
        if participant_form.is_valid(): #and address_form.is_valid() and city_form.is_valid() and country_form.is_valid():
            participant_form.save()

        registered = True
            #return HttpResponse("Thank you for registering for this event.")
            #return HttpResponseRedirect(reverse('aff_site:register'))
    else:
        #No HTTP request so just return a blank form
        participant_form = NewParticipant()

    # This is the render and context dictionary to feed
    # back to the registration.html file page
    return render (request, 'aff_site/registration.html',
                                {'participant_form':participant_form,
                                'registered':registered})
                                 #'address_form':address_form,
