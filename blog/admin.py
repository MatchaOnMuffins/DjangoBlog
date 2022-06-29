from django.contrib import admin

from .models import Post, Comments

admin.site.register(Post)
admin.site.register(Comments)  # Register the model in the admin site
