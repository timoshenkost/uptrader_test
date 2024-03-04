from django.db import models
from django.urls import reverse

from .services.utils import unique_slugify


class MenuItem(models.Model):
    """
    Модель отдельного пункта в меню
    """

    name = models.CharField(verbose_name='Имя', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True)
    menu_name = models.CharField(verbose_name='Название меню', max_length=255)
    parent = models.ForeignKey('self', verbose_name='Родительский пункт', null=True, blank=True,
                               on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:menu_item', kwargs={'menu_name': self.menu_name, 'item_slug': self.slug})


    def save(self, *args, **kwargs):
        self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)
