from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.views import LoginView  
from .forms import LoginForm, UserRegistrationForm


class RegisterCheck(View):
      def post(self, request):
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                  new_user = user_form.save(commit=False)
                  new_user.set_password(user_form.cleaned_data['password'])
                  new_user.save()
            return redirect('/')

class LoginView(LoginView):
      template_name = 'login.html'

