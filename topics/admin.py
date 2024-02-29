from django.contrib import admin

from topics.models import Topic, UsefulLink

admin.site.register(Topic)
admin.site.register(UsefulLink)
