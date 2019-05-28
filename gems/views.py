from django.shortcuts import render, get_object_or_404, redirect
import random

from .models import Gem
# Create your views here.


def gem_list(request):
    gems = Gem.objects.all()
    return render(request, 'gems/gem_list.html', {'gems': gems})


def gem_detail(request, name):
    gem = get_object_or_404(Gem, name=name)
    blacklist = ('_state', 'id', 'name', 'image_filename', 'image_caption')
    return render(request, 'gems/gem_detail.html', {
        'gem': gem.__dict__.items(), 'blacklist': blacklist, 'obj': gem})


def gem_random(request):
    count = Gem.objects.all().count()
    pk = random.randint(1, count)
    gem = Gem.objects.get(pk=pk)
    return redirect('detail', name=gem.name)

