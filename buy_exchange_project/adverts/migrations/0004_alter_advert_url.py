# Generated by Django 4.0.6 on 2022-08-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_advert_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='url',
            field=models.SlugField(max_length=60),
        ),
    ]
