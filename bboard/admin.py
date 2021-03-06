from django.contrib import admin

from .models import Notes


class Dbadmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Notes, Dbadmin)