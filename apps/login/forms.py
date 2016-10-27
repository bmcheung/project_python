from django import forms
from .models import Pet, User


class PetForm(forms.Form):
    class Meta:
        model = Pet
        fields = '__all__'
