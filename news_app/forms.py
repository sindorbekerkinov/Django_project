from .models import FormModel
from django import forms

class InputForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = "__all__"