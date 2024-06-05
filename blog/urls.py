from django.urls import path
from blog.apps import BlogConfig
from blog.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', ArticleCreateView.as_view(), name='blog_create'),
    path('', ArticleListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]

