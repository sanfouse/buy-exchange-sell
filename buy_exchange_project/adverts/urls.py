from django.urls import path

from . import views

urlpatterns = [
      path('<int:pk>/', views.AdvertDetail.as_view(), name='advert_detail'),
      path('', views.AdvertList.as_view(), name='advert_list'),
      path('add_item/', views.AdvertAdd.as_view())
]
