from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
      user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
      profile_image = models.ImageField(verbose_name='Аватарка', upload_to='profile_image', blank=True, null=True)

