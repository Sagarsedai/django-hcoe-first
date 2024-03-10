from django.contrib import admin

from .models import Blog, BlogTag, BlogAuthors

admin.site.register([BlogTag, Blog, BlogAuthors])
