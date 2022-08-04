from django.urls import path
from django.views.generic import TemplateView
from .forms import UserRegistrationForm, LoginForm
from .views import RegisterCheck, LoginView

urlpatterns = [
      path('register/', TemplateView.as_view(
                  template_name='users/register.html', 
                  extra_context={
                              'form': UserRegistrationForm()
                        }
            )
      ),
      path('register/check/', RegisterCheck.as_view()),
      path('login/', TemplateView.as_view(
                  template_name='users/login.html', 
                  extra_context={
                              'form': LoginForm()
                        }
            )
      ),
      path('login/check/', LoginView.as_view())      
]