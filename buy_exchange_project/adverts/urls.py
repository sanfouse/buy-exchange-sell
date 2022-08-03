from django.urls import path
from . import views
from django.views.generic import TemplateView
from .models import Category

urlpatterns = [
      path('<int:pk>/', views.AdvertDetail.as_view(), name='advert_detail'),
      path('', views.AdvertList.as_view(), name='advert_list'),
      path('add_item/', TemplateView.as_view(
                        template_name = 'adverts/advert_add.html',
                        extra_context={"categories": Category.objects.all()}           
                  )
            ),
]