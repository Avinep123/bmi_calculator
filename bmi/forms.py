# bmi/forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'gender', 'height', 'weight']
        labels = {
            'height': 'Height (in cm)',
            'weight': 'Weight (in kg)',
        }
