from django.shortcuts import render, redirect
from .models import Person
from django.contrib import messages
from .forms import PersonCreateForm, PersonUpdateForm


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
            Person.objects.create(firstname=cd['firstname'],lastname=cd['lastname'],phone=cd['phone'],email=cd['email'],)
            messages.success(request, 'Person Created Successfully', 'success')
            return redirect('home')
    else:
        form = PersonCreateForm()
        return render(request, 'create.html', {'form': form})




