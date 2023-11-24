from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return  render(request,"loginapp/index.html")

def signIn(request):
    return render(request,"loginapp/signIn.html")

def signup(request):
    return render(request,"loginapp/signup.html")

def signout(request):
    pass

