from django.views.generic import DetailView,ListView

from util.views import UtilListView,UtilDetailView
from .models import Post,Category


class PostView(UtilDetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostListView(UtilListView):
    model = Post
    paginate_by = 10
    category_model = Category
    template_name = 'posts/list.html'


post_detail = PostView.as_view()
posts_list = PostListView.as_view()