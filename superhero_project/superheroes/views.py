from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
# Create your views here.

def index (request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)
    

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == "POST":
        # save the form contents as a new db object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name = name, alter_ego = alter_ego, primary_ability = primary, secondary_ability = secondary, catch_phrase = catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def update(request, hero_id):
    single_hero = Superhero.objects.get(pk = hero_id)
    if request.method == 'Post':
        update_name = request.POST.get('name')
        update_alter_ego = request.POST.get('alter_ego')
        update_primary = request.POST.get('primary')
        update_secondary = request.POST.get('secondary')
        update_catchphrase = request.POST.get('catcphrase')
        updated_hero = Superhero(name = update_name, alter_ego = update_alter_ego, primary_ability = update_primary, secondary_ability = update_secondary, catch_phrase = update_catchphrase)
        updated_hero.save()
        Superhero.delete(single_hero)
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return HttpResponseRedirect(reverse('superheroes/update.html'))


def delete(request, hero_id):
    archnemesis = Superhero.objects.get(pk = hero_id)
    if request.method == 'Post':
        Superhero.delete(archnemesis)
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return HttpResponseRedirect(reverse('superheroes/delete.html'))