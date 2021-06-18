from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Photos(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'photos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[self.pk])
