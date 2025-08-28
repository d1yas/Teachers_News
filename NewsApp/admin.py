from django.contrib import admin
from .models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image_preview")
    search_fields = ("title", "description")
    list_filter = ("title",)

    def image_preview(self, obj):
        if obj.image:
            return f"<img src='{obj.image.url}' width='80' height='60' style='object-fit: cover;' />"
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = "Image"
