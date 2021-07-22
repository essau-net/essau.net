# Utilities
from datetime import datetime
from iso639 import languages as iso_languages
from markdown import markdown
from pathlib import Path

# Django
from django.forms import ValidationError

# local
from posts.models import Posts, Languages


BASE_DIR = Path(__file__).resolve().parent.parent
TMP_FILES = BASE_DIR / 'static/posts_files'


class LanguagesManager:
    """Language manager data"""

    def __init__(self, language=''):
        """constructor"""
        self.__language = language.title()

    @property
    def language(self):
        """language's getter"""
        return self.__language

    @language.setter
    def language(self, language):
        """language's setter
        if language is in  spanish or french translate to english"""
        language = language.title()
        # Language of my interest
        if language == 'Español' or language == 'Espanol':
            language = 'Spanish'
        elif language == 'Frances' or language == 'Francés' or language == 'Français':
            language = 'French'
        try:
            self.__language = iso_languages.get(name=language).bibliographic
        except KeyError:
            raise ValidationError('Please check the language writing')

    @staticmethod
    def language_in_ISO_format(self, language):
        """Check if the class language variable is in ISO format"""
        if len(language) == 3:
            try:
                iso_languages.get(bibliographic=language.lower())
                return True
            except KeyError:
                return False
        else:
            return False

    @staticmethod
    def iso_to_language(self, language):
        """Take a variable with iso format language and return its name"""
        iso_format = LanguagesManager.language_in_ISO_format(self, language)
        if iso_format:
            language = iso_languages.get(bibliographic=language.lower())
            return language.name

    def language_exist(self):
        """Check if the language exist, if not create it.
        Return info language's field"""

        try:
            language = Languages.objects.get(language=self.language)

        except Languages.DoesNotExist:
            language = Languages(language=self.language)
            language.save()

        return language

    def language_to_iso(self, language):
        """Convert a name language to ISO standard"""
        iso_format = LanguagesManager.language_in_ISO_format(self, language)
        if iso_format is False:
            self.language = language
            return self.language
        else:
            return self.language

    def all_iso_to_languages(self, all_obj_languages):
        """Take a list of languages in ISO format and return a list with language's name"""
        all_languages = [LanguagesManager.iso_to_language(self, language_obj.language)
                         for language_obj in all_obj_languages]
        return all_languages


class PostsManager:

    def __init__(self, title, content):
        self.__title = title
        self.__content = content
        self.__path_markdown_file = ""
        self.__path_html_file = ""

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @property
    def path_markdown_file(self):
        return self.__path_markdown_file

    @property
    def path_html_file(self):
        return self.__path_html_file

    @path_markdown_file.setter
    def path_markdown_file(self, path):
        self.__path_markdown_file = path

    @path_html_file.setter
    def path_html_file(self, path):
        self.__path_html_file = path

    def createMarkdownFile(self):
        global TMP_FILES
        
        unique_identifier = str(datetime.now())
        unique_identifier = unique_identifier.replace(' ', '--')

        name_file =  self.title + unique_identifier + '.md'
        name_file.strip(' ')

        path = TMP_FILES / name_file

        with open(path, 'w+') as markdownFile:
            markdownFile.write(self.content)

        self.path_markdown_file = path

    def createHTMLFile(self):
        global TMP_FILES

        unique_identifier = str(datetime.now())
        unique_identifier = unique_identifier.replace(' ', '--')

        name_file = self.title + unique_identifier + '.html'
        name_file.strip(' ')

        path = TMP_FILES / name_file

        with open(self.path_markdown_file, 'r') as md_file: 
            md_content = md_file.read()
            html_content = markdown(md_content)

        with open(path, 'w') as html_file:
            html_file.write(html_content)

        self.path_html_file = path


