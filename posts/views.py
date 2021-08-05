# utils
# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, TemplateView
from django.views.generic.edit import FormMixin

# Local models
from posts.forms import CreatePostForm, NewCommentForm
from posts.managers import LanguagesManager, PostsManager, CommentsManager
from posts.models import Posts, Languages, Categories, Tags, Comments


#POSTS
class CreatePostView(LoginRequiredMixin, FormView):
    """Create a new Post"""

    template_name = "posts/new.html"
    form_class = CreatePostForm
    success_url = reverse_lazy("posts:feed")

    def get_context_data(self, **kwargs):
        """Get languages, categories and tags saved in database"""

        context = super().get_context_data(**kwargs)

        all_languages = Languages.objects.all()
        languages_manager = LanguagesManager()

        context["languages"] = languages_manager.all_iso_to_languages(all_languages)
        context["categories"] = Categories.objects.all()
        context["tags"] = Tags.objects.all()

        return context

    def form_valid(self, form):
        """Create a new post"""

        user_id = self.request.user
        form.save(user_id)
        return super().form_valid(form)


class PostFeedView(ListView):
    """Return published posts"""

    template_name = "posts/feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        """Get all post published with its respective data"""

        posts_manager = PostsManager()
    
        posts = posts_manager.get_post_data()
        posts = posts_manager.post_data_to_array(posts=posts)

        return posts


class PostDetailView(FormMixin, DetailView):
    """Post detail view"""
    
    context_object_name = "post"
    form_class = NewCommentForm
    model = Comments
    queryset = Posts.objects.all()
    template_name = "posts/detail.html"

    def form_valid(self, form):
        """Create a new comment"""
        
        post = super().get_object()
        user = self.request.user
        
        form.save(user=user, post=post)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Get post's comments and the current user"""

        data =  super().get_context_data(**kwargs)

        post_id = data['object'].id

        comments_manager = CommentsManager(post_id=post_id)
        comments_data = comments_manager.get_post_comments()
        
        data["comments"] = comments_manager.comments_data_to_array(comments_data=comments_data)
        data["user"] = self.request.user

        return data

    def get_success_url(self):
        pk =  super().get_object().pk
        return reverse_lazy('posts:detail', kwargs={'pk': pk})
    
    def post (self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form=form)
        else:
            return self.form_invalid()

#About its creator
class AboutMe(TemplateView):
    template_name = 'me.html'