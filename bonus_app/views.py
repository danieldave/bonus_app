from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bonuses.models import Bonus

@login_required
def dashboard(request):
    bonus = Bonus.objects.filter(user=request.user).first()
    return render(request, "dashboard.html", {"bonus": bonus})
