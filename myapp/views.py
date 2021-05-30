from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")
def myfunctionabout(request):
    return HttpResponse("About Response")
def add(request,a,b):
    return HttpResponse(a+b)
def intro(request,name,age):
    mydictionary={
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)
def myfirstpage(request):
    return render(request, 'index.html')
def mysecondpage(request):
    return render(request, 'second.html')
def mythirdpage(request):
    var="Hello world"
    greeting="hola"
    fruits=["apple", "banana", "kiwi", "pear"]
    num1, num2 = 3,5
    ans=num1>num2
    mydictionary={
        "var":var,
        "msg":greeting,
        "myfruits":fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans
    }
    return render(request, 'third.html', context=mydictionary)

def myimagepage(request):
    return render(request, 'imagepage.html')
def myimagepage2(request):
    return render(request, 'imagepage2.html')
def myimagepage3(request):
    return render(request, 'imagepage3.html')
def myimagepage4(request):
    return render(request, 'imagepage4.html')

def myimagepage5(request, imagename):
    myimagename=str(imagename);
    myimagename=myimagename.lower();
    if myimagename == 'circle':
        var=True
    elif myimagename == 'triangle':
        var=False
    mydictionary={
        "var":var
    }
    return render(request, 'imagepage5.html', context=mydictionary)