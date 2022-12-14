from django.shortcuts import render, redirect
from django.contrib import messages, auth 
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('register')
            
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exist')
                    return redirect('register')
                
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email, last_name=last_name)
                    user.save()
                    messages.success(request, 'You can now login')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register') 

    else:
        return render(request, 'accounts/register.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged In')
            return redirect('dashboard') 
        else:
            messages.success(request, 'Invalid Login')
            return render(request, 'accounts/login.html') 


    return render(request, 'accounts/login.html')   

def dashboard(request):
    return render(request, 'accounts/dashboard.html')  
