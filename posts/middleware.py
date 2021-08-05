"""Restrict post's actions to different user's kind"""

#Django
from django.shortcuts import redirect
from django.urls import reverse

class CreatePostMiddleware:
    """Create post middleware
    
    Ensure that just users who are staff, super users and active can create new posts"""

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed each request to create new post view"""
        user = request.user

        if request.path == reverse('posts:new_post'):
            if not user.is_authenticated or not user.is_staff or not user.is_active:
                return redirect('posts:feed')
        
        response = self.get_response(request)
        return response