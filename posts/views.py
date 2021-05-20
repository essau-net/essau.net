#utils
#django 
from django.shortcuts import render
from posts import models  
#third apps
#local apps


# Create your views here.
def list_posts(request):
    """List existing posts"""
    posts = models.Posts.objects.all()
    print(posts)
    return render(request, 'posts/feed.html', {'posts': posts})