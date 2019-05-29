from django.shortcuts import render, get_object_or_404, redirect
import random

from .models import Gem
# Create your views here.


def gem_list(request):
    """Root view grabs all objects and passes to gem_list view"""
    gems = Gem.objects.all()
    return render(request, 'gems/gem_list.html', {'gems': gems})


def gem_detail(request, name):
    """
    Gets an object in the form of /object and gets the record
    or throws 404.  Blacklist is meant for the keys not to display.
    passes the object details as a dict, blacklist, and object
    """
    gem = get_object_or_404(Gem, name=name)
    blacklist = ('_state', 'id', 'name', 'image_filename', 'image_caption')
    return render(request, 'gems/gem_detail.html', {
        'gem': gem.__dict__.items(), 'blacklist': blacklist, 'obj': gem})


def gem_random(request):
    """
    Generate random integer from 1 to number of objects and passes
    that object's name to the detail view
    """
    count = Gem.objects.all().count()
    pk = random.randint(1, count)
    gem = Gem.objects.get(pk=pk)
    return redirect('detail', name=gem.name)

