from django.contrib import admin
from .models import Post


class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')


admin.site.register(Post, postAdmin) 