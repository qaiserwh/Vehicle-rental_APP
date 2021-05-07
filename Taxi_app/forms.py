

from Taxi_app.models import Taxie,Buse,Truckse,Drivers
from django import forms
from . models import Buse, Taxie



class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class TaxiForm(forms.ModelForm):
    class Meta:
        model =Taxie
        fields =[
            'client_name',
            'phonenumber',
            'age_of_driver',
            'location',
            'To',
        ] 
        

        widgets ={
            'client_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'age_of_driver': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'----'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':' location'}),
            'To': forms.TextInput(attrs={'class':'form-control', 'placeholder':'To'}),
        }

class BusForm(forms.ModelForm):
    class Meta:
        model =Buse
        fields =[
            'client_name',
            'phonenumber',
            'location',
            'To',
        ] 
        

        widgets ={
            'client_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':' location'}),
            'To': forms.TextInput(attrs={'class':'form-control', 'placeholder':'To'}),
        }


class TrucksForm(forms.ModelForm):
    class Meta:
        model =Truckse
        fields =[
            'client_name',
            'phonenumber',
            'Type_of_load',
            'location',
            'To',
        ] 
        

        widgets ={
            'client_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'Type_of_load': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':' location'}),
            'To': forms.TextInput(attrs={'class':'form-control','placeholder':'To'}),
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model =Drivers
        fields =[
            'name',
            'age',
            'email',
            'phonenumber',
            'Type_of_car',
            'carnumber',
        ] 
        

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'age'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':' email'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'Type_of_car': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of car'}),
            'carnumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'----'}),
        }