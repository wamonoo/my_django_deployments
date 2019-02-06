from django import forms
from aff_site.models import Participant #,Address,City,Country

class NewParticipant(forms.ModelForm):
    class Meta:
        model = Participant
        #exclude = ['address']
        fields = '__all__'
'''
class NewAddress(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['city']
        #fields = '__all__'
class NewCity(forms.ModelForm):
    class Meta:
        model = City
        exclude = ['country']
        #fields = '__all__'
class NewCountry(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
'''
