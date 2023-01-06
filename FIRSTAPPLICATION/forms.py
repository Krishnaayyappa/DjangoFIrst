from django import forms
from .models import Name

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = "__all__"