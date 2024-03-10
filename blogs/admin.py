from django.contrib import admin

from .models import Blog, BlogTag

admin.site.register([BlogTag, Blog])
