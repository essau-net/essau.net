# Utilities
from datetime import date
from iso639 import languages as iso_languages
from markdown import markdown
from pathlib import Path

# Django
from django.db import connection
from django.forms import ValidationError

# local
from posts.models import Posts, Languages


BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_FILES = BASE_DIR / "static/posts_files"


class LanguagesManager:
    """Language manager data"""

    def __init__(self, language=""):
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
        if language == "Español" or language == "Espanol":
            language = "Spanish"
        elif language == "Frances" or language == "Francés" or language == "Français":
            language = "French"
        try:
            self.__language = iso_languages.get(name=language).bibliographic
        except KeyError:
            raise ValidationError("Please check the language writing")

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
        all_languages = [
            LanguagesManager.iso_to_language(self, language_obj.language)
            for language_obj in all_obj_languages
        ]
        return all_languages


class PostsManager:
    def __init__(self, title="", content=""):
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

    def get_ListPost_data(self):
        
        cursor = connection.cursor()

        query = "SELECT posts.id," \
            "posts.title," \
            "posts.publicated_at," \
            "tags.tag," \
            "categories.category," \
            "languages.`language`" \
            "FROM posts" \
              " INNER JOIN languages ON languages.id = posts.language_id" \
              " INNER JOIN categories ON categories.id = posts.category_id" \
              " INNER JOIN posts_tags ON posts_tags.post_id = posts.id" \
              " INNER JOIN tags ON tags.id = posts_tags.tag_id" \
            " ORDER BY posts.publicated_at"
        
        cursor.execute(query)

        posts_data = cursor.fetchall()
        post_data_dic = {}

        for post_data in posts_data:
            title = post_data[1]

            if title in post_data_dic:
                post_data_dic[title]['tags'].append(post_data[3])
            else:
                post_data_dic[title] = {
                    'title': post_data[1],
                    'publicated_at': post_data[2],
                    'tags': [post_data[3]],
                    'category': post_data[4],
                    'language': post_data[5]
                }
            for key, value in post_data_dic.items():
                print(f'\n\n\n {value["category"]}\n\n\n')
        return post_data_dic

    def createMarkdownFile(self):
        global POSTS_FILES

        unique_identifier = str(date.today())

        name_file = self.title + unique_identifier + ".md"

        path = POSTS_FILES / name_file

        with open(path, "w+") as markdownFile:
            markdownFile.write(self.content)

        self.path_markdown_file = name_file

    def createHTMLFile(self):
        global POSTS_FILES

        unique_identifier = str(date.today())

        name_file = self.title + unique_identifier + ".html"

        path_html = POSTS_FILES / name_file
        path_markdown = POSTS_FILES / self.path_markdown_file

        with open(path_markdown, "r") as md_file:
            md_content = md_file.read()
            html_content = markdown(md_content)

        with open(path_html, "w") as html_file:
            html_file.write(html_content)

        self.path_html_file = name_file
