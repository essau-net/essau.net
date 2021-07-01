#Utilities
from iso639 import languages as iso_languages

#Django
from django.forms import ValidationError

#local
from metadata_post.models import Languages as LanguagesModel
from posts.models import Categories as CategoriesModel

class DataManager:
    """Manage data between models and views"""

    class Languages:
        """Manage Language data"""


        def __init__(self, language=''):
            """constructor"""
            self.__language = language.title()


        @property
        def language(self):
            """language getter"""
            return self.__language


        @language.setter
        def language(self, language):
            """languages setter
            if language is in  spanish or french translate to english"""

            #Language of my interest
            if language == 'Español' or language == 'Espanol':
                language = 'Spanish'
            elif language == 'Frances' or language == 'Francés' or language == 'Français':
                language = 'French'

            try: 
                self.__language = iso_languages.get(name=language.title()).bibliographic
            except KeyError:
                raise ValidationError('Please check the language writing')


        @staticmethod
        def language_in_ISO_format(self, language):
            """Check if the class language variable is in ISO format"""

            if len(language) == 3:
                try:
                    iso_languages.get(bibliographic=language.lower())
                    return True

                except KeyError: return False


        @staticmethod
        def iso_to_language(self, language):
            """Take a variable with iso format language and return its name"""

            iso_format = Languages.language_in_ISO_format(self, language)

            if iso_format:
                language = iso_languages.get(bibliographic=language.lower())
                return  language.name

        def language_exist(self):
            """Check if the language exist, if not create it.
            Return info language's field"""

            lang_exist = LanguagesModel.objects.filter(language=self.language)

            if lang_exist:
                return lang_exist
            else:
                return LanguagesModel.objects.create(language=self.language)


        def language_to_iso(self, language):
            """Convert a name language to ISO standard"""

            iso_format = Languages.language_in_ISO_format(self,language)

            if iso_format is False:
                return language
            else:
                language = iso_languages.get(bibliographic=language.lower())

                return language



        def all_iso_to_languages(self, all_obj_languages):
            """Take a list of languages in ISO format and return a list with language's name""" 
            all_languages = [Languages.iso_to_language(self, language_obj.language) 
                             for language_obj in all_obj_languages]

            return all_languages


    class Categories:
        """Manage categories data"""

        def __init__(self, category_name=''):
            self.__category_name =  category_name

        @property
        def category_name(self):
            return self.__category_name

        @category_name.setter
        def category_name(self, category_name):
            self.__category_name = category_name

        def category_exist(self, category_name):
            """Check i category exist, if not create it
            return info category's field"""

            category_exist = CategoriesModel.objects.filter(category_name=category_name)

            if category_exist:
                return category_exist
            else:
                return CategoriesModel.objects.create(category_name=category_name)



