from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'age', 'years_married', 'religiousness', 'rating_of_marriage']