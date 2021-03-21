from django.shortcuts import render
from django.views.static import serve
from django.views.generic import ListView, DetailView

from .models import Event
# Create your views here.


class EventView(ListView):
    model = Event
    ordering = ['-date_added']
    template_name = 'event/event.html'


class HomeView(ListView):
    model = Event
    ordering = ['date_added']
    template_name = 'index.html'


