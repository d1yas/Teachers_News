from django.contrib import admin
from .models import TeachersModel


@admin.register(TeachersModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "middle_name", "gender", "date_of_birth")
    search_fields = ("first_name", "last_name", "middle_name")
    list_filter = ("gender", "date_of_birth")
    fields = (
        "first_name",
        "last_name",
        "middle_name",
        "date_of_birth",
        "gender",
        "bio",
        "photo",
    )
    
    readonly_fields = ("photo_preview",)

    def photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="80" style="border-radius: 8px;" />'
        return "No Photo"
    photo_preview.allow_tags = True
    photo_preview.short_description = "Photo Preview"