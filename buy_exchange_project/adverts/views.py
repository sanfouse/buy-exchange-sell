from django.views.generic import ListView, DetailView

from .models import Advert

class AdvertList(ListView):
      model = Advert

class AdvertDetail(DetailView):
      model = Advert
