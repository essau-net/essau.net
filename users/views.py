"""Users views"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy
from django.views.generic import FormView

#Forms
from users.forms import SignupForm


class LoginView(auth_views.LoginView):
    """Login view"""

    template_name = 'users/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view """

    template_name = 'users/logged_out.html'

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        """Save form data"""

        import pdb; pdb.set_trace()
        form.save()
        return super().form_valid(form)
        