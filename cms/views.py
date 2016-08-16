from django.views.generic import DetailView,ListView

from util.views import UtilDetailView
from .models import Page


class PageView(UtilDetailView):
    model = Page
    template_name = 'cms/detail.html'


page_detail = PageView.as_view()