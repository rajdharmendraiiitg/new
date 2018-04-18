from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm,RentForm
from .models import CarData,RentData
from django.db import connection
from datetime import datetime

def home(request):
    return render(request, 'registerpage/homepage.html')

def fb(request):
    return render(request, 'registerpage/formpage.html')

def home2(request):
    return render(request, 'registerpage/loginhome.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'registerpage/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                name = request.user.username
                diction={'name':name}
                return render(request, 'registerpage/loginhome.html',diction)
            else:
                return render(request, 'registerpage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registerpage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registerpage/login.html')


def login_user1(request):
    print("car lelo")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
	print("1")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("2")
            if user.is_active:
                login(request, user)
                return render(request, 'registerpage/loginhome1.html')
            else:
                return render(request, 'registerpage/login1.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registerpage/login1.html', {'error_message': 'Invalid login'})
    return render(request, 'registerpage/login1.html')




def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return render(request, 'registerpage/login.html')
    context = {
        "form": form,
    }
    return render(request, 'registerpage/register.html', context)


def faq(request):
    return render(request, 'registerpage/faq.html')


def showcar(request):
    all_car = CarData.objects.all()
    context = {
        "all_car": all_car
    }
    return render(request, 'registerpage/car.html', context)


def confirmation(request):
    return render(request, 'registerpage/confirm.html')


def create_rentdata(request):
    if not request.user.is_authenticated():
        return render(request, 'registerpage/login.html')
    else:
        form = RentForm(request.POST or None)
        if form.is_valid():
            rentdata = form.save(commit=False)
            rentdata.username = request.user
            rentdata.carname = form.cleaned_data['carname']
            if rentdata.carname == 'Ford Mustang' or rentdata.carname == 'Chevrolet Impala':
                rentdata.cost = 25000
            elif rentdata.carname == 'Nissan Versa' or rentdata.carname == 'Chrysler 200':
                rentdata.cost = 15000
            elif rentdata.carname == 'Toyota Corolla':
                rentdata.cost = 15000
            elif rentdata.carname == 'Jeep Wrangle' or rentdata.carname == 'Chevrolet Spark':
                rentdata.cost = 5000
            elif rentdata.carname == 'Chevrolet Cruze':
                rentdata.cost = 5000
            rentdata.save()
            return render(request, 'registerpage/confirm.html', {'rentdata': rentdata})
        all_car = CarData.objects.all()
        context = {
            "form": form,
            "all_car": all_car
        }
        return render(request, 'registerpage/rentdata_form.html', context)


def history(request):
    if not request.user.is_authenticated():
        return render(request, 'registerpage/login.html')
    else:
        cursor= connection.cursor()
        form = RentForm(request.POST ,None)
        user_name=request.user.username
        #user_name =user.username
        print(user_name)
        no=cursor.execute('''SELECT username,id from registerpage_rentdata ''')
        transaction_id=[]
        c=0
        for i in no:
            print(i)
            for j in i:
                if(j==user_name):
                    c+=1
        diction={'no':c}
        return render(request, 'registerpage/history.html', diction)


def currently_booked(request):
    if not request.user.is_authenticated():
        return render(request, 'registerpage/login.html')
    else:
        car={'name':[]}
        user_name=request.user.username
        for p in RentData.objects.raw('''SELECT 1 as id ,username, carname from registerpage_rentdata '''):
            if(p.username==user_name):
                print(p.carname)
                car['name'].append(p.carname)
        return render(request, 'registerpage/currently_booked.html', car)


def create_adddata(request):
    if not request.user.is_authenticated():
        return render(request, 'registerpage/login.html')
    else:
        form = RentForm(request.POST or None)
        if form.is_valid():
            rentdata = form.save(commit=False)
            rentdata.username = request.user
            rentdata.carname = form.cleaned_data['carname']
            if rentdata.carname == 'Ford Mustang' or rentdata.carname == 'Chevrolet Impala':
                rentdata.cost = 25000
            elif rentdata.carname == 'Nissan Versa' or rentdata.carname == 'Chrysler 200':
                rentdata.cost = 15000
            elif rentdata.carname == 'Toyota Corolla':
                rentdata.cost = 15000
            elif rentdata.carname == 'Jeep Wrangle' or rentdata.carname == 'Chevrolet Spark':
                rentdata.cost = 5000
            elif rentdata.carname == 'Chevrolet Cruze':
                rentdata.cost = 5000
            rentdata.save()
            return render(request, 'registerpage/confirm.html', {'adddata': adddata})
        all_car = CarData.objects.all()
        context = {
            "form": form,
            "all_car": all_car
        }
        return render(request, 'registerpage/add_car.html', context)

def fb(request):
    return render(request, 'registerpage/formpage.html')
