from django.contrib import admin

from .models import Blog_post, Comments

admin.site.register(Blog_post)
admin.site.register(Comments)