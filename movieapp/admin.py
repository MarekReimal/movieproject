from django.contrib import admin
from . models import * # kõik mudelid saavad siia faili

# Register your models here.

# et teha super juser enne seda on vaja teha makemigration

admin.site.register(Country) # näita Country model
admin.site.register(Movie)