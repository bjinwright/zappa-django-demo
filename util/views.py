from django.http import Http404
from django.views.generic import ListView, DetailView
from django.utils.translation import ugettext as _


class UtilDetailView(DetailView):

    def get_object(self, queryset=None):
        try:
            # Get the single item from the filtered queryset
            obj = self.model.objects.get(slug=self.kwargs.get('slug'),active=True)
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class UtilListView(ListView):

    def get_queryset(self):
        if self.kwargs.get('slug'):
            category = self.category_model.objects.get(
                slug=self.kwargs.get('slug'))
            return self.model.objects.filter(
                categories=category.pk).order_by('-date_created')
        return self.model.objects.all().order_by('-date_created')