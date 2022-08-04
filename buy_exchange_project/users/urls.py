from django.urls import path

from .views import LoginView, RegisterView, LogOutView

urlpatterns = [
      path('register/', RegisterView.as_view()),
      path('login/', LoginView.as_view()),
      path('log_out/', LogOutView.as_view()),
      # path('<int: pk>/')      
]
