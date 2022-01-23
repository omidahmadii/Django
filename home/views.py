from django.shortcuts import render, redirect
from .models import Person
from django.contrib import messages
from .forms import PersonCreateForm

def home(request):
    all = Person.objects.all()
    return render(request, 'home.html', {'persons': all})


def detail(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, 'detail.html', {'person': person })

def delete(request, person_id):
    Person.objects.get(id=person_id).delete()
    messages.success(request, 'Person Deleted Successfully', 'success')
    #messages.success(request, 'Person Deleted Successfully', 'warning')
    return redirect('home')



def create(request):
    form = PersonCreateForm()
    return render(request, 'create.html', {'form': form})




