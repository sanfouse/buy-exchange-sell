from django.db import models

class Category(models.Model):
      title = models.CharField(verbose_name='Название', max_length=60)
      url = models.SlugField(max_length=60)

      def __str__(self):
            return self.title

      class Meta:
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'

class Advert(models.Model):
      title = models.CharField(verbose_name='Название', max_length=60)
      price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
      category = models.ManyToManyField(Category, verbose_name='Категория', related_name='category')
      description = models.TextField(verbose_name='Описание')
      date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)

      def __str__(self):
            return self.title

      class Meta:
            verbose_name = 'Товар'
            verbose_name_plural = 'Товары'


class Image(models.Model):
      image = models.ImageField(verbose_name='Изображение', upload_to='image')
      advert = models.ForeignKey(Advert, verbose_name='Товар', on_delete=models.CASCADE)
      
      class Meta:
            verbose_name = 'Картинку'
            verbose_name_plural = 'Картинки'
      
