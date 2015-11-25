import sys

# SETTINGS 

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="nomoresecrets",
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=[],
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'django-example.sqlite3'
        }
    },
    DEBUG_PROPAGATE_EXCEPTIONS=True
)


# MODELS

from django.db import models

class ThingModel(models.Model):
    
    class Meta:
        app_label = 'main'
        
    foo = models.IntegerField()
    bar = models.CharField(max_length=100)


class StuffModel(models.Model):
    
    class Meta:
        app_label = 'main'
        
    baz = models.ForeignKey(ThingModel)
    qux = models.CharField(max_length=1000)
    

# VIEWS

from django.conf.urls import url
from django.http import HttpResponse
from tranquil.contexts import MultiContext
from tranquil.django.contexts import DjangoModelContext, DjangoMultiContext

class RootContext(DjangoMultiContext):
    pass

@RootContext.register('thing')
class ThingContext(DjangoModelContext):
    model = ThingModel
    
@RootContext.register('stuff')
class StuffContext(DjangoModelContext):
    model = StuffModel
    
print repr(RootContext._registry)

urlpatterns = (
    url(r'^api/1$', RootContext.as_view()),
)


# STARTUP

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
