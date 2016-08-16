from django.conf.urls import url
from .views import page_detail


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', page_detail, name='page_detail'),
]