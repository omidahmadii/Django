from django import forms
from .models import Person


class PersonCreateForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)


class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        #fields = ('firstname', 'lastname', 'phone', 'email')
        fields = '__all__'
