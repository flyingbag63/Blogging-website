from django.contrib import admin
from .models import PostComment, BlogPost, Blogger

# Register your models here.

admin.site.register(PostComment)
admin.site.register(BlogPost)
admin.site.register(Blogger)
