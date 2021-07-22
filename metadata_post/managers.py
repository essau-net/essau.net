#local
from posts.models import Languages, Categories, Tags
from metadata_post.models import PostsLanguages, PostsTags


class TagsManager:
    """Tags data manager """
    
    def __init__(self, tags):
        self.__tags = tags.split(',')

    @property
    def tags(self):
        """Tags' getter"""
        return self.__tags

    @tags.setter
    def tags(self, tags):
        self.__tags = tags.split(',')
    
    @staticmethod
    def tag_exist(self, tag):

        try:
            local_tag = Tags.objects.get(tag=tag)

        except Tags.DoesNotExist: 
            local_tag = Tags(tag=tag)
            local_tag.save()
        
        return local_tag

    def tags_exist(self):
        tags = [TagsManager.tag_exist(self, tag) 
                for tag in self.tags]
        return tags


class CategoriesManager:
    """Categories  data manager"""

    
    def __init__(self, category=''):
        self.__category =  category   

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    def category_exist(self):
        """Check if category exist, if not create it
        return info category's field"""
        
        try:
            category =  Categories.objects.get(category=self.category)
        
        except Categories.DoesNotExist:
            category =  Categories(category=self.category)
            category.save()

        return category
        

class PostsTagsManager:
    
    def __init__(self, post, tags):
        self.__post = post
        self.__tags = tags

    @property
    def post(self):
        return self.__post

    @property
    def tags(self):
        return self.__tags

    def createTables(self):
        for tag in self.tags:
            PostsTags.objects.create(post=self.post, tag=tag)


class PostsLanguagesManager:
    """Posts_languages manager data"""
    def __init__(self, post, language):
        self.__post = post
        self.__language = language

    @property
    def post(self):
        return self.__post
    
    @property
    def language(self):
        return self.__language

    def createTable(self):
        PostsLanguages.objects.create(post=self.post, language=self.language)
