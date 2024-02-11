from django.contrib import admin
from .models import Post


# admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("title",)
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Post, PostAdmin)
