from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewParticipant


def home(request):
    return render (request, 'aff_site/main_page.html')

def contacts(request):
    return render (request, 'aff_site/contacts.html')

def overview(request):
    return render (request, 'aff_site/overview.html')

def events(request):
    return render(request, 'aff_site/events.html')

def register(request):

    if request.method == "POST":
        participant_form = NewParticipant(request.POST or None)
#extras from here
        if participant_form.is_valid(): #and address_form.is_valid() and city_form.is_valid() and country_form.is_valid():
            participant_form.save()
            return HttpResponseRedirect(reverse('aff_site:home'))
    else:
        participant_form = NewParticipant()
    return render (request, 'registration.html',
                                {'participant_form':participant_form})
                                 #'address_form':address_form,
