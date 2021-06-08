

from Taxi_app.models import Taxie,Buse,Truckse,Drivers
from django import forms
from . models import Buse, Taxie, VipBuse



class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class TaxiForm(forms.ModelForm):
    class Meta:
        model =Taxie
        fields =[
            'client_name',
            'phonenumber',
            'time',
            'location',
            'To',
        ] 
        

        widgets ={
            'client_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'time':forms.Select(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':' location'}),
            'To': forms.TextInput(attrs={'class':'form-control', 'placeholder':'To'}),
        }

class BusForm(forms.ModelForm):
    class Meta:
        model =Buse
        fields =[
            'client_name',
            'phonenumber',
            'time',
            'location',
            'To',
        ] 
        

        widgets ={
            'client_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'time':forms.Select(attrs={'class':'form-control'}),
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
            'time',
            'location',
            'To',
        ] 
        

        widgets ={
            'client_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'Type_of_load': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'time':forms.Select(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':' location'}),
            'To': forms.TextInput(attrs={'class':'form-control','placeholder':'To'}),
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model =Drivers
        fields =[
            'name',
            'email',
            'phonenumber',
            'Type_of_car',
            'carnumber',
        ] 
        

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':' email'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'Type_of_car': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of car'}),
            'carnumber': forms.TextInput(attrs={'class':'form-control', 'placeholder':'----'}),
        }
        


class VipBusForm(forms.ModelForm):
    class Meta:
        model =VipBuse
        fields =[
            'clientname',
            'phonenumber',
            'price',
            'time',
            'location',
            'To',
        ] 
        

        widgets ={
            'clientname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'price':forms.Select(attrs={'class':'form-control'}),
            'time':forms.Select(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':' location'}),
            'To': forms.TextInput(attrs={'class':'form-control', 'placeholder':'To'}),
        }

