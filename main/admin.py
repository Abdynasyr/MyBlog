from django.contrib import admin

from .models import *


class PostImageInline(admin.TabularInline):
    model = PostImage
    max_name = 10
    min_name = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, ]


admin.site.register(Category)
