from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
        

def registration(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is Already Taken ')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is Already Taken ')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,name=name)
                user.save();
                messages.info(request,'User is Created Successfully')
                return redirect('login')
        else:
            messages.info(request,'Password is Not Matching')
            return redirect('registration')
        return redirect('/')
    else:
        return render(request, 'registration.html')

