
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return  render(request,"loginapp/index.html")

def signIn(request):
    return render(request,"loginapp/signIn.html")

def signup(request):
    if request.method == 'POST':
        # user_name = request.POST.get(user_name) or
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(user_name,email,password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()

        messages.success(request,"your account has been created")
        return redirect('signIn')
        

    return render(request,"loginapp/signup.html")

def signout(request):
    pass

