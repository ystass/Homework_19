from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'created_at', 'published', 'number_views',)
    success_url = reverse_lazy('blog:list')
