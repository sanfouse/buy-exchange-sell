from django.contrib import admin
from .models import Category, Advert, Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Advert)
admin.site.register(Image)
