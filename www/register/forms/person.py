from django import forms
from django_countries.widgets import CountrySelectWidget

from ..models import Person

__all__ = ['PersonForm']


class PersonForm(forms.ModelForm):
    country = forms.CharField(widget=CountrySelectWidget())
    class Meta:
        model = Person
        fields = '__all__'
