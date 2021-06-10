#utils
#django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

#Local models
from posts.forms import NewPostForm
from posts.models import Posts, Tags, Categories


class PostFeedView(ListView):
    """Return published posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created_at',)
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new Post"""

    template_name='posts/new.html'
    form_class = NewPostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user, tags and categories to context"""

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()

        return context
        
