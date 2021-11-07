from django.db import models
from django.urls import reverse


class Constellation(models.Model):
    name_ru = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    short_name = models.CharField(max_length=3, unique=True)
    square = models.IntegerField()
    total_stars = models.IntegerField()
    symbol = models.CharField(max_length=200)
    zodiac = models.BooleanField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('constellation_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Constellation'
        verbose_name_plural = 'Constellations'


class Star(models.Model):
    name = models.CharField(max_length=50)
    constellation = models.ForeignKey('Constellation', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
