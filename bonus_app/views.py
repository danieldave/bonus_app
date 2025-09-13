from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from bonuses.models import Bonus

@login_required
def dashboard(request):
    bonus = Bonus.objects.filter(user=request.user).first()
    return render(request, "dashboard.html", {"bonus": bonus})


def login_redirect(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect("bonus_list")  # admin dashboard
    return redirect("user_dashboard")  # normal user