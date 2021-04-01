from django.contrib import admin
from django.urls import path
from pages.views import about_view
from news.views import EventView, HomeView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventView.as_view(), name='event'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
