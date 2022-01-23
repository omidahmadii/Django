from django import forms


class PersonCreateForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()