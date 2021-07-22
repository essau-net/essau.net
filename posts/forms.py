"""Posts Forms"""

# Utilities
from iso639 import languages as iso_languages

# Django
from django import forms
from django.forms import fields

# Local
from metadata_post.managers import  TagsManager, CategoriesManager, PostsTagsManager, PostsLanguagesManager
from posts.managers import LanguagesManager, PostsManager

from posts.models import Posts


class CreatePostForm(forms.Form):

    title = forms.CharField(
        required=True,
        min_length=1,
        max_length=150,
    )

    language = forms.CharField(
        required=True,
        min_length=3,
    )

    category = forms.CharField(
        required=True,
        min_length=1,
        max_length=30,
    )

    tags = forms.CharField(required=True)

    content = forms.CharField(
        required=True,
        min_length=1,
        widget=forms.Textarea(),
    )

    image = forms.ImageField(required=False)

    def clean_language(self):
        """Link language with the post"""

        language = self.cleaned_data['language']

        manager_language = LanguagesManager(language=language)
        manager_language.language_to_iso(language)

        language = manager_language.language_exist()

        return language

    def clean_category(self):
        """Link category with the post"""

        category = self.cleaned_data['category']

        categories_manager = CategoriesManager(category.lower())
        category = categories_manager.category_exist()

        return category

    def clean_tags(self):

        tags = self.cleaned_data['tags']

        tags_manager = TagsManager(tags.lower())
        tags = tags_manager.tags_exist()

        return tags

    def clean(self):
        data = super().clean()
        
        post_manager = PostsManager(title=data['title'], content=data['content'])
        post_manager.createMarkdownFile()
        post_manager.createHTMLFile()

        data['url_markdown_file'] = post_manager.path_markdown_file
        data['url_html_file'] = post_manager.path_html_file

        return data

    def save(self, user_id):
        """Create data and link them to my post"""

        data = self.cleaned_data
        data['user'] = user_id

        language = data['language']
        tags = data['tags']
        image_data = data['image']

        data.pop('language')
        data.pop('tags')
        data.pop('image')
        data.pop('content')

        post = Posts(**data)
        post.save()


