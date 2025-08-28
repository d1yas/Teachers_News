from django.contrib import admin
from .models import TeachersModel

@admin.register(TeachersModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "middle_name", "gender", "date_of_birth", "photo_path")
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
        "photo_path",
    )

    readonly_fields = ("photo_path",)

    def photo_path(self, obj):
        if obj.photo:
            return obj.photo.url  # yoki obj.photo.path agar serverdagi path kerak bo‘lsa
        return "No Photo"

    photo_path.short_description = "Photo Path"
