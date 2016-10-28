from django import forms
from .models import Pet, User


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
