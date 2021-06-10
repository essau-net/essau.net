"""Posts Forms"""

#Django 
from django import forms
from django.forms import fields

#Local
from posts.models import Languages, Posts, Tags, Categories

class NewPostForm(forms.ModelForm):
    """Create new post form"""

    title = forms.CharField(
        required=True,
        min_length=1,
        max_length=150,
    )

    language = forms.CharField(
        required=True,
        min_length=3,
    )

    category_name = forms.CharField(
        required=True,
        min_length=1,
        max_length=30
    )


    tags = forms.JSONField()

    content = forms.CharField(
        required=True,
        min_length=1,
        widget=forms.Textarea
    )

    img = forms.ImageField()

    def clean_language():
        pass

    def clean_category_name():
        pass

    def clean_tags():
        pass


















































