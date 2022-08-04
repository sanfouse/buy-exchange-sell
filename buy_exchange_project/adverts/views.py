from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import AdvertForm
from .models import Advert, Category, Image


class AdvertList(ListView):
      model = Advert


class AdvertDetail(DetailView):
      model = Advert


class AdvertAdd(LoginRequiredMixin, View):
      def post(self, request):
            form = AdvertForm(request.POST)
            if form.is_valid():
                  title = form.cleaned_data.get('title')
                  price = form.cleaned_data.get('price')
                  description = form.cleaned_data.get('description')
                  object = Advert.objects.create(title=title,price=price,description=description, user=request.user)
                  for category_title in request.POST.getlist('category'):
                        object.category.add(Category.objects.get(title=category_title))
                  for image in request.FILES.getlist('image'):
                        Image.objects.create(image=image, advert=object)
            return redirect('/')

      def get(self, request):
            return render(request, 'adverts/advert_add.html', {'categories': Category.objects.all()})
            
            