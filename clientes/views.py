from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .form import PersonForm

# Create your views here.


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {"persons": persons})


def person_new(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
        print(form['salary'])
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    
    return render(request, 'person_form.html', {"form": form})

def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    print(request.method)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    
    return render(request, 'person_delete.html', {'form': form})