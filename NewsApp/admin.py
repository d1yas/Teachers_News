from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title_truncated", "description_truncated", "image_preview")
    search_fields = ("title", "description")
    list_filter = ("title",)  # Remove created_at since it doesn't exist
    readonly_fields = ("image_preview",)
    
    def title_truncated(self, obj):
        """Display truncated title for better readability"""
        if obj.title and len(obj.title) > 50:
            return f"{obj.title[:50]}..."
        return obj.title or "No Title"
    title_truncated.short_description = "Title"
    
    def description_truncated(self, obj):
        """Display truncated description for better readability"""
        if obj.description and len(obj.description) > 100:
            return f"{obj.description[:100]}..."
        return obj.description or "No Description"
    description_truncated.short_description = "Description"

    def image_preview(self, obj):
        """Display image thumbnail with better styling"""
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit: cover; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
                obj.image.url
            )
        return format_html('<span style="color: #999;">No Image</span>')
    image_preview.short_description = "Preview"