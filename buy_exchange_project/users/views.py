from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from .forms import UserRegistrationForm


class RegisterView(View):
      def post(self, request):
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                  new_user = user_form.save(commit=False)
                  new_user.set_password(user_form.cleaned_data['password'])
                  new_user.save()
            return redirect('/')
      def get(self, request):
            return render(request, 'users/register.html', {'form': UserRegistrationForm()})

class LoginView(LoginView):
      template_name = 'users/login.html'

class LogOutView(LoginRequiredMixin, LogoutView):
      pass
      
