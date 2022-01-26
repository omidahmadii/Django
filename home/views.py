from django.shortcuts import render, redirect
from .models import Person, Province, City
from django.contrib import messages
from .forms import PersonCreateForm, PersonUpdateForm, ProvinceAddProvinceForm, CityAddCityForm


def home(request):
    all = Person.objects.all()
    return render(request, 'home.html', {'persons': all})


def detail(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, 'detail.html', {'person': person })


def delete(request, person_id):
    Person.objects.get(id=person_id).delete()
    messages.success(request, 'Person Deleted Successfully', 'success')
    # messages.success(request, 'Person Deleted Successfully', 'warning')
    return redirect('home')


def update(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method =='POST':
        form = PersonUpdateForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person Updated Successfully', 'success')
            return redirect('home')
    else:
        form = PersonUpdateForm(instance=person)
        return render(request, 'update.html', {'form': form})


def create(request):
    if request.method == "POST":
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Person.objects.create(firstname=cd['firstname'],lastname=cd['lastname'])
            messages.success(request, 'Person Created Successfully', 'success')
            return redirect('home')
    else:
        form = PersonCreateForm()
        return render(request, 'create.html', {'form': form})


def add_province(request):
    if request.method == "POST":
        form = ProvinceAddProvinceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Province.objects.create(provice_per_name=cd['provice_per_name'],provice_eng_name=cd['provice_eng_name'])
            messages.success(request, 'Province Added Successfully', 'success')
            return redirect('home')
    else:
        form = ProvinceAddProvinceForm()
        return render(request, 'add_province.html', {'form': form})

def add_city(request):
    if request.method == "POST":
        form = CityAddCityForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            City.objects.create(city_per_name=cd['city_per_name'],city_eng_name=cd['city_eng_name'])
            messages.success(request, 'City Added Successfully', 'success')
            return redirect('home')
    else:
        form = CityAddCityForm()
        return render(request, 'add_city.html', {'form': form})

