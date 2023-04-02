from django.contrib import admin

from .models import Topic, Entry
admin.site.register(Entry)

from learning_logs.models import Topic
admin.site.register(Topic)
