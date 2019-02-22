from django.http import HttpResponse

from .models import World, Plot
from .forms import WorldForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import json

class ListView(generic.ListView):
    template_name = 'lifegame/index.html'
    queryset = World.objects.order_by('name')

class CreateView(generic.CreateView):
    template_name = 'lifegame/create.html'
    form_class = WorldForm

class DetailView(generic.DetailView):
    model = World
    template_name = 'lifegame/world.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        world = get_object_or_404(World, alias=self.kwargs.get("slug"))
        context['x'] = range(world.width)
        context['y'] = range(world.height)
        context['data'] = json.loads(world.data)

        return context

    def get_object(self):
        return get_object_or_404(World, alias=self.kwargs.get("slug"))

class DeleteView(generic.DeleteView):
    template_name = 'lifegame/delete.html'

    def get_object(self):
        return get_object_or_404(World, alias=self.kwargs.get("slug"))

    def get_success_url(self):
        return reverse('world-list')
