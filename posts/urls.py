from django.conf.urls import url

from .views import post_detail,posts_list
urlpatterns = [
    url(r'^posts/$', posts_list, name='posts_list'),
    url(r'^posts/(?P<slug>[\w-]+)/$', posts_list, name='category_detail'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
]