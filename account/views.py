from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def login_required_decorate(func):
    return login_required(func,login_url='login_page')

@login_required_decorate
def logout_page(request):
    logout(request)
    return redirect("login_page")

def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,password=password, username=username)
        if user is not None:
            login(request, user)
        return redirect("home")

    return render(request,"account/login.html")

@login_required_decorate
def home(request):
    return render(request,'news/index.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_page')
    template_name = "account/signup.html"