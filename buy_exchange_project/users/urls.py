from django.urls import path

from .views import *

urlpatterns = [
      path('register/', RegisterView.as_view(), name='register'),
      path('login/', LoginView.as_view(), name='login'),
      path('log_out/', LogOutView.as_view(), name='log_out'),
      path('', UserAdvert.as_view(), name='user'),
      path('<int:pk>', DetailUserView.as_view(), name='user_id')      
]
