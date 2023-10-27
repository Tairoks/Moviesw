from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Category', max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.pk} - {self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
