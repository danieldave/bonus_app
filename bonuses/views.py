from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import BonusAssignForm
from .models import Bonus
from .forms import BonusForm

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


# Helper to restrict access
def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def assign_bonus(request):
    if request.method == "POST":
        form = BonusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bonus assigned successfully!")
            return redirect("bonus_list")
    else:
        form = BonusForm()
    return render(request, "bonuses/assign_bonus.html", {"form": form})

@login_required
@user_passes_test(is_admin)
def bonus_list(request):
    bonuses = Bonus.objects.select_related("user").all().order_by("-created_at")
    return render(request, "bonuses/bonus_list.html", {"bonuses": bonuses})

@login_required
def user_dashboard(request):
    bonuses = request.user.bonuses.all().order_by("-created_at")
    return render(request, "bonuses/user_dashboard.html", {"bonuses": bonuses})


@login_required
def dashboard(request):
    # calculate bonus balance here
    bonus_balance = request.user.bonuses.aggregate(total=models.Sum('amount'))['total'] or 0
    return render(request, 'bonuses/dashboard.html', {
        'bonus_balance': bonus_balance
    })  