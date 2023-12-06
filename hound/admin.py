from django.contrib import admin
from .models import Publisher, Episode, Show

class ShowAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Show)
admin.site.register(Episode)