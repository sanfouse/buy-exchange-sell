from adverts.models import Advert
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from .forms import ProfileUserForm

from .forms import UserRegistrationForm


class RegisterView(View):
      def post(self, request):
            user_form = UserRegistrationForm(request.POST)
            user_image = ProfileUserForm(request.POST, request.FILES)
            if user_form.is_valid() and user_image.is_valid():
                  new_user = user_form.save(commit=False)
                  new_user.set_password(user_form.cleaned_data['password'])
                  new_image = user_image.save(commit=False)
                  new_image.user = new_user
                  new_user.save()
                  new_image.save()
            return redirect('/')
      def get(self, request):
            return render(request, 'users/register.html', {'form': UserRegistrationForm(), 'image': ProfileUserForm()})


class LoginView(LoginView):
      template_name = 'users/login.html'


class LogOutView(LoginRequiredMixin, LogoutView):
      pass
      

class UserAdvert(ListView):
      template_name = 'users/useradvert_list.html'
      def get_queryset(self):
            return Advert.objects.filter(user=self.request.user)

class DetailUserView(View):
      def get(self, request, pk):
            user = User.objects.get(id=pk)
            return render(request, 'users/useradvert_list.html', {
                              'user': user,
                              'advert_list': Advert.objects.filter(user=user)
                        }
                  )

