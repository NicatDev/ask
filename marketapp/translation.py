from modeltranslation.translator import TranslationOptions,register, translator
from marketapp.models import Category,Tag,Team,Training,TrainingSection,Article,News,Show,Services,Psychology,PsychologySection,ServiceSection

class ArticleTranslationOption(TranslationOptions):
    fields = ('title','content','content_2')

class ShowNewsTranslationOption(TranslationOptions):
    fields = ('title','content')

class ServicePsychologyTrainingTranslationOption(TranslationOptions):
    fields = ('name','description','title')
  
class SectionTranslationOption(TranslationOptions):
    fields = ('title','description')

class PsySectionTranslationOption(TranslationOptions):
    fields = ('title','description','bottomDescription')

class CategoryTagTranslationOption(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTagTranslationOption)
translator.register(Tag, CategoryTagTranslationOption)

translator.register(Article, ArticleTranslationOption)
translator.register(News, ShowNewsTranslationOption)
translator.register(Show, ShowNewsTranslationOption)

translator.register(Services, ServicePsychologyTrainingTranslationOption)
translator.register(Psychology, ServicePsychologyTrainingTranslationOption)
translator.register(Training, ServicePsychologyTrainingTranslationOption)

translator.register(ServiceSection, SectionTranslationOption)
translator.register(PsychologySection, PsySectionTranslationOption)
translator.register(TrainingSection, SectionTranslationOption)