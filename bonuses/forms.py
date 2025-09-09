from django import forms
from django.contrib.auth.models import User
from .models import Bonus

class BonusAssignForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Bonus
        fields = ["user", "amount", "reason", "status"]
