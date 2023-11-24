from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hello")

def signIn(request):
    return render(request,"loginapp/signIn.html")

def signout(request):
    return render(request,"loginapp/signout.html")

def signup(request):
    return render(request,"loginapp/signup.html")