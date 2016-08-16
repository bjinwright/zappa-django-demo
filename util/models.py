from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class UtilModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    active = models.BooleanField(default=False)


    class Meta:
        abstract = True


class TitleSlugModel(UtilModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


    class Meta:
        abstract = True


class TitleSlugBodyModel(TitleSlugModel):
    body = models.TextField()


    class Meta:
        abstract = True