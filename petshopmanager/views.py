from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms import formset_factory
from django.utils import timezone

from .models import Animal, AnimalForm, Equipment, EquipementForm


def index(request):
    animals_list = Animal.objects.all()
    equipments_list = Equipment.objects.all()
    context = {'animals_list': animals_list,
               'equipments_list':equipments_list}
    return render(request, 'petshopmanager/index.html', context)


def animals_list(request):
    list = Animal.objects.all()
    form = AnimalForm(initial={'place': Equipment.objects.filter(type=Equipment.LITTER).filter(availability=True).first()})
    context = {'animals_list': list,
               'form': form}
    return render(request, 'petshopmanager/animals_list.html', context)


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    context = {'animal': animal}
    return render(request, 'petshopmanager/animal_detail.html', context)


def animal_add(request):
    a = AnimalForm(request.POST)
    a.save()
    return HttpResponseRedirect(reverse('petshopmanager:animals_list'))


def feed(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if animal.state == Animal.HUNGRY:
        try:
            target_location = Equipment.objects.filter(type=Equipment.FEEDER).filter(availability=True).first()
        except:
            context = {'animal': animal, 'error_message': "Aucune mangeoire n'est disponible."}
            return render(request, 'petshopmanager/animal_detail.html', context)
        animal.change_place(target_location)
        animal.change_state(Animal.SATED)
        return HttpResponseRedirect(reverse('petshopmanager:animal_detail', args=(pk,)))
    else:
        context = {'animal': animal, 'error_message': "L'animal {} n'a pas faim.".format( animal.name)}
        return render(request, 'petshopmanager/animal_detail.html', context)


def entertain(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if animal.state == Animal.SATED:
        try:
            target_location = Equipment.objects.filter(type=Equipment.WHEEL).filter(availability=True).first()
        except:
            context = {'animal': animal, 'error_message': "Aucune roue n'est disponible."}
            return render(request, 'petshopmanager/animal_detail.html', context)
        animal.change_place(target_location)
        animal.change_state(Animal.TIRED)
        return HttpResponseRedirect(reverse('petshopmanager:animal_detail', args=(pk,)))
    else:
        context = {'animal': animal, 'error_message': "L'animal {} n'est pas en état de faire du sport.".format( animal.name)}
        return render(request, 'petshopmanager/animal_detail.html', context)


def sleep(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if animal.state == Animal.TIRED:
        try:
            target_location = Equipment.objects.filter(type=Equipment.NEST).filter(availability=True).first()
        except:
            context = {'animal': animal, 'error_message': "Aucun nid n'est disponible."}
            return render(request, 'petshopmanager/animal_detail.html', context)
        animal.change_place(target_location)
        animal.change_state(Animal.SLEEP)
        return HttpResponseRedirect(reverse('petshopmanager:animal_detail', args=(pk,)))
    else:
        context = {'animal': animal, 'error_message': "L'animal {} n'est pas fatigué.".format( animal.name)}
        return render(request, 'petshopmanager/animal_detail.html', context)


def wake_up(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if animal.state == Animal.SLEEP:
        target_location = Equipment.objects.filter(type=Equipment.LITTER).filter(availability=True).first()
        animal.change_place(target_location)
        animal.change_state(Animal.HUNGRY)
        return HttpResponseRedirect(reverse('petshopmanager:animal_detail', args=(pk,)))
    else:
        context = {'animal': animal, 'error_message': "L'animal {} ne dort pas".format( animal.name)}
        return render(request, 'petshopmanager/animal_detail.html', context)


def equipments_list(request):
    list = Equipment.objects.all()
    used_by = {e.id: e.used_by() for e in list}
    form = EquipementForm()
    context = {'equipments_list': list,
               'used_by': used_by,
               'form': form}
    return render(request, 'petshopmanager/equipments_list.html', context)


def equipment_detail(request, pk):
    equipment= get_object_or_404(Equipment, pk=pk)
    used_by = equipment.used_by()
    context = {'equipment': equipment,
               'used_by': used_by}
    return render(request, 'petshopmanager/equipment_detail.html', context)


def equipment_add(request):
    e = EquipementForm(request.POST)
    e.save()
    return HttpResponseRedirect(reverse('petshopmanager:equipments_list'))