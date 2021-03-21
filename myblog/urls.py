from django.contrib import admin
from django.urls import path
from pages.views import about_view
from news.views import EventView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventView.as_view(), name='event'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
]
