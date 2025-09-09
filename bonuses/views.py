from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import BonusAssignForm
from .models import Bonus

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



# only allow staff/admins
def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def assign_bonus(request):
    if request.method == "POST":
        form = BonusAssignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bonus assigned successfully!")
            return redirect("assign_bonus")
    else:
        form = BonusAssignForm()
    return render(request, "bonuses/assign_bonus.html", {"form": form})
@user_passes_test(is_admin)
def bonus_history(request):
    bonuses = Bonus.objects.all().order_by("-created_at")
    return render(request, "bonuses/bonus_history.html", {"bonuses": bonuses})

