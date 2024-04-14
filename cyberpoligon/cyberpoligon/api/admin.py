from django.contrib import admin

from .models import MarkdownContent, Image, Paper

# admin.site.register(MarkdownContent)
# admin.site.register(Image)
@admin.register(MarkdownContent)
class MarkdownContentAdmin(admin.ModelAdmin):
    list_display = ("title", "markdown_content")

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "file_name", "mime_type", "md5_hash", "created_at")

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "created_at")
