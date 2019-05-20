from django import forms
from .models import HappinessLevel


class HappinessLevelForm(forms.ModelForm):
    class Meta:
        model = HappinessLevel
        fields = ('level',)
