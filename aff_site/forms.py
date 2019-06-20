from django import forms
from aff_site.models import Participant, Portal_user #,Address,City,Country
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewParticipant(forms.ModelForm):
    class Meta:
        model = Participant
        #exclude = ['address']
        fields = '__all__'

'''
class SignupForm(forms.ModelForm):
    class Meta:
        model = Portal_user
        widgets = {'password':forms.PasswordInput, 'password2':forms.PasswordInput}
        fields = '__all__'
'''
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


'''class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
'''
