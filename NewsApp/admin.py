from django.contrib import admin
from .models import NewsModel

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title_truncated", "description_truncated", "image_path")
    search_fields = ("title", "description")
    list_filter = ("title",)
    readonly_fields = ("image_path",)
    
    def title_truncated(self, obj):
        if obj.title and len(obj.title) > 50:
            return f"{obj.title[:50]}..."
        return obj.title or "No Title"
    title_truncated.short_description = "Title"
    
    def description_truncated(self, obj):
        if obj.description and len(obj.description) > 100:
            return f"{obj.description[:100]}..."
        return obj.description or "No Description"
    description_truncated.short_description = "Description"

    def image_path(self, obj):
        if obj.image:
            return obj.image.url  # brauzer uchun URL
            # return obj.image.path  # serverdagi to‘liq path kerak bo‘lsa
        return "No Image"
    image_path.short_description = "Image Path"
