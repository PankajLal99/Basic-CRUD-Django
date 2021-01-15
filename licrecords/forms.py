from django  import forms
from django.forms import fields
from . import models

class customerform(forms.ModelForm):
    class Meta:
        model=models.Cutomer
        fields='__all__'