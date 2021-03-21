from django.shortcuts import render
from django.views.static import serve
from django.views.generic import ListView, DetailView

from .models import Event
# Create your views here.


def event_view_page(request):
    obj = Event.objects.get().order_by('id')

    last_three = Event.objects.filter(since=since).order_by('-id')[:10]
    last_ten_in_ascending_order = reversed(last_three)

    context = {
        "object": obj
    }
    return render(request, 'event/event.html', context)


class HomeView(ListView):
    model = Event
    ordering = ['-date_added']
    template_name = 'index.html'


