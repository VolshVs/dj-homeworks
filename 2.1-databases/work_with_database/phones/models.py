from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=55, unique=True, verbose_name='Имя (name)')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена (price)')
    image = models.ImageField(verbose_name='Фоточки')
    release_date = models.DateField(default=None, blank=True, verbose_name='Дата (release_date)')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=55, unique=True, db_index=True, verbose_name="slug")

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, {self.slug}'

    # def get_absolute_url(self):
    #     return reverse('product', kwargs={'slug': self.slug})
