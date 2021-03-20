from django.shortcuts import render
from django.views.static import serve

from .models import Event
# Create your views here.


def event_view_page(request):
    obj = Event.objects.get(id=3)

    context = {
        "object": obj
    }
    return render(request, 'event/event.html', context)
