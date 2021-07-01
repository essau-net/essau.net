from iso639 import languages
try: 
    result= languages.get(bibliographic='fre'.lower())
    
except KeyError:
    print(f'\n\n\n check if you write correctly the language \n\n\n')
