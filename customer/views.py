from django.shortcuts import render , redirect
from customer.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# Create your views here.

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username=username , password=password)
        if user:
            login(request,user)
            return redirect('post-index')
        else:
            return render(request , 'customer/signin.html' , {'error':'Invalid username or password'})
    return render(request,'customer/signin.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        repeated_password = request.POST['repeated_password']
        if password != repeated_password:
            messages.error(request, 'psswords are not macht')
            return render(request , 'customer/signup.html')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request , 'user exists')
                return render(request , 'customer/signup.html')
            else:
                user = User.objects.create(username=username , password=password)
                user.set_password(password)
                user.save()
                customer = Customer.objects.create(user=user)
                messages.success(request , 'account creaeted')
                return render(request , 'customer/signin.html')
            
    return render(request , 'customer/signup.html')


def logout(request):
    auth_logout(request)
    return redirect("signin")
            

