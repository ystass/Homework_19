from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'created_at', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'created_at', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog_list')


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog_list')
