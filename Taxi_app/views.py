from Taxi_app.models import Buse, Drivers, Taxie, Truckse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from . forms import  TaxiForm,BusForm ,TrucksForm,DriverForm ,AdminLoginForm
# Create your views here.
def tables(request):
    context={
        'taxi':Taxie.objects.all(),
        'bus':Buse.objects.all(),
        'truck':Truckse.objects.all()


    }
    return render(request,'tables.html',context)
def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('tables')
    context = {'forms': forms}
    return render(request, 'login.html', context)
def index(request):
    
    return render(request,'index.html')

def Taxiorder(request):
    if request.method =='POST':
        Taxi_Order =TaxiForm(request.POST, request.FILES)
        if Taxi_Order.is_valid():
            Taxi_Order.save()
            return  redirect('index')
            

    context ={
        'name_of_clint': Taxie.objects.all(),
        'the_number_phone_of_clint':Taxie.objects.all(),
        'forms':TaxiForm(),
        'location':Taxie.objects.all(),
        'To':Taxie.objects.all(),    
    }

    return render(request,'Taxiorder.html',context)


def Trucksorder(request):
    if request.method =='POST':
        Trucks_Order =TrucksForm(request.POST, request.FILES)
        if Trucks_Order.is_valid():
            Trucks_Order.save()
            return  redirect('index')
            

    context ={
        'name_of_clint':Truckse.objects.all(),
        'the_number_phone_of_clint':Truckse.objects.all(),
        'forms':TrucksForm(),

        'location':Truckse.objects.all(),
        'To':Truckse.objects.all(),

        
    }

    return render(request,'Trucksorder.html',context)



def Busorder(request):
    if request.method =='POST':
        Bus_Order =BusForm(request.POST, request.FILES)
        if Bus_Order.is_valid():
            Bus_Order.save()
            return  redirect('index')
            

    context ={
        'name_of_clint': Buse.objects.all(),
        'the_number_phone_of_clint':Buse.objects.all(),
        'forms':BusForm(),
        'age_of_driver':Taxie.objects.all(),
        'location':Buse.objects.all(),
        'To':Buse.objects.all(),

        
    }

    return render(request,'Busorder.html',context)

def Driversorder(request):
    if request.method =='POST':
        Drivers_Order =BusForm(request.POST, request.FILES)
        if Drivers_Order.is_valid():
            Drivers_Order.save()
            return  redirect('index')
            

    context ={
        'name': Drivers.objects.all(),
        'age': Drivers.objects.all(),
        'email': Drivers.objects.all(),
        'forms':DriverForm(),
        'phonenumber': Drivers.objects.all(),
        'Type_of_car': Drivers.objects.all(),
        'carnumber': Drivers.objects.all(),

        
    }

    return render(request,'Driversorder.html',context)


def price(request):
    return render(request,'price.html')
def about(request):

    return render(request,'about.html')