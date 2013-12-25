from django_toronto.settings import *


MIDDLEWARE_CLASSES += ('staticbuilder.middleware.BuildOnRequest', )
