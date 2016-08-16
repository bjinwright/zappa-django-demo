from __future__ import unicode_literals

from django.urls import reverse_lazy

from util.models import TitleSlugModel,TitleSlugBodyModel


class Page(TitleSlugBodyModel):

    def get_absolute_url(self):
        return reverse_lazy('page_detail',args=[self.slug])