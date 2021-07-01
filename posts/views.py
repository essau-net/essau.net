#utils
#django 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

#Local models
from posts.forms import CreatePostForm
from metadata_post.managers import DataManager
from posts.models import Posts


class PostFeedView(ListView):
    """Return published posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created_at',)
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, FormView):
    """Create a new Post"""

    template_name='posts/new.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:feed')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     data_manager = DataManager()
    #     manager_language = ManagementLanguages()

    #     context['languages'] = manager_language.all_iso_to_languages(all_languages)

        

        # return context

    def form_valid(self, form):        
        """Save form data"""

        form.save()
        return super().form_valid(form)