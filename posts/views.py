# utils
# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView

# Local models
from posts.forms import CreatePostForm
from posts.managers import LanguagesManager
from posts.models import Posts, Languages, Categories, Tags


class PostFeedView(ListView):
    """Return published posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created_at',)
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, FormView):
    """Create a new Post"""

    template_name = 'posts/new.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_languages = Languages.objects.all()
        languages_manager = LanguagesManager()

        context['languages'] = languages_manager.all_iso_to_languages(
                                all_languages)
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()

        return context

    def form_valid(self, form):
        """Save form data"""

        user_id = self.request.user
        form.save(user_id)
        return super().form_valid(form)
