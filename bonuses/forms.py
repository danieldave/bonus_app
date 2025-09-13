from django import forms
from django.contrib.auth.models import User
from .models import Bonus


class BonusAssignForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Bonus
        fields = ["user", "amount", "reason", "status"]



class BonusForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = ["user", "amount", "reason", "status"]

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"})
    )
    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    reason = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    status = forms.ChoiceField(
        choices=Bonus.STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
