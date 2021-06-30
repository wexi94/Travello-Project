from django.shortcuts import render,HttpResponse


def home(request):
    return render(request, 'home.html',{'name': 'Ahmed Ali ' })


def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request, 'add.html',{'result':res})

