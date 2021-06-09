from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *
# Create your views here.
def error_404_view(request, exception):
    return render(request, '404.html')

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
def myform(request):
    return render(request, 'myform.html')
def submitmyform(request):
    mydictionary={
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)
def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary={
                "form": FeedbackForm()
            }
            Errors=[]
            errorflag=False
            if title != title.upper():
                errorflag=True
                errormsg='Title should be in Capital'
                Errors.append(errormsg)
            import re
            # https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
            # https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
            regex ='^(\w|\.|\-)+[@](\w|\.|\-)+[.]\w{2,3}$'
            if not re.search(regex, email):
                errorflag=True
                errormsg='Email address is not valid'
                Errors.append(errormsg)
            if errorflag!=True:
                mydictionary["success"]=True
                mydictionary["successmsg"]="Form submitted"
            mydictionary["error"]=errorflag
            mydictionary["errors"]=Errors       
            print("postttt")
            return render(request, 'myform2.html', context=mydictionary)
    elif request.method=='GET':
        form = FeedbackForm()
        mydictionary={
            'form':form
        }
        print("gettttt")
        return render(request, 'myform2.html', context=mydictionary)