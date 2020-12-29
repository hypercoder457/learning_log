from django.contrib import admin

from .models import Entry, Topic


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    list_display = ['text', 'date_added']
    inlines = [EntryInline]


admin.site.register(Topic, TopicAdmin)
