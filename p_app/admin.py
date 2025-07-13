from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Saying)
# admin.site.register(Tag)
admin.site.register(SavedSayings)
admin.site.register(Reflections)