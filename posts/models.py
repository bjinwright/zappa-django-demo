from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from util.models import TitleSlugModel,TitleSlugBodyModel


class Category(TitleSlugModel):

    def get_absolute_url(self):
        return reverse('category_detail',args=[self.slug])


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(TitleSlugBodyModel):
    categories = models.ManyToManyField(Category,related_name='post_category')

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


