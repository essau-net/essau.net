"""Posts Forms"""

#Utilities
from iso639 import languages as iso_languages

#Django 
from django import forms
from django.forms import fields

#Local




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

    category_name = forms.CharField(
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

    img = forms.ImageField(required=False)

    # def clean_language(self):
    #     """Link language with the post"""

    #     language = self.cleaned_data['language']

    #     manager_language = ManagementLanguages(language=language)
    #     manager_language.language_to_iso(language)
    #     language = manager_language.language_exist()

    #     print(language)

    #     return language

    def clean_tags(self):

        tags = self.cleaned_data['tags']
        print(f'\n\n\n {type(tags)}\n\n\n ')

        return tags

    # def clean_category_name(self):
    #     """Link category with the post"""

    #     category_name = self.cleaned_data['category_name']
    #     category_exist = Categories.objects.filter(category_name=category_name)

    #     if category_exist:
    #         category_name = category_exist
    #     else:
    #         category_name = Categories.objects.create(category_name=category_name)

    #     return category_name

    # def clean_tags(self):
    #     pass

    def save(self): 
        """Create data and link them to my post"""
        
        data = self.cleaned_data
        print(f'\n\n\n {data} \n\n\n')

    










































