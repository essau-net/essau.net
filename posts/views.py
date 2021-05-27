#utils
#django 
from django.shortcuts import render
from django.views.generic import ListView

#Local models
from posts.models import Posts


class PostFeedView(ListView):
    """Retun published posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created_at',)
    context_object_name = 'posts'