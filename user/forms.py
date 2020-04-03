from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Location

class NewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']
        widgets = {
            'username': forms.TextInput(attrs = {
                'class':'form-control',
                'placeholder':'Username',
            }),
            'email': forms.TextInput(attrs = {
                'class':'form-control',
                'type': 'email',
                'placeholder':'Email',
                'required':'True',
            }),
        }
        
class ClientLocation(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['hall_or_hostel','room_number','mobile_number']
        widgets = {
            'hall_or_hostel': forms.TextInput(attrs ={
                'class':'form-control',
                'placeholder':'Hall or Hostel',
                
            }),
            'room_number': forms.TextInput(attrs ={
                'class':'form-control',
                'placeholder':'Room Number',
            }),
            'mobile_number': forms.TextInput(attrs ={
                'class':'form-control',
                'type':'tel',
                'placeholder':'Mobile Number',
                'maxlenght':'10',
            }),
            
        }
        help_texts = {
            'mobile_number':"Please provide the school's vodafone number if possible.",
        }
        
class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        widgets = {
            'first_name': forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'username': forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs = {
                'required': 'true',
                'class': 'form-control',
                'type':'email',
            }),
        }