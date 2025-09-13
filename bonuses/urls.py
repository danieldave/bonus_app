from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("assign-bonus/", views.assign_bonus, name="assign_bonus"),
    path("list/", views.bonus_list, name="bonus_list"),
    path("dashboard/", views.user_dashboard, name="user_dashboard"),
]


