from django import forms
from .models import Person, Province, City


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')

        #fields = '__all__'
"""    
class PersonCreateForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)
"""

class ProvinceAddProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = '__all__'


class CityAddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        #fields = ('firstname', 'lastname', 'phone', 'email')
        fields = '__all__'
