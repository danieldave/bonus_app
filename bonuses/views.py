from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")

def login_view(request):
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

