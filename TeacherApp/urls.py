from django.urls import path
from .views import TeacherAPIView, All_TeacherListAPIView

urlpatterns = [
    path("all_teachers/", All_TeacherListAPIView.as_view(), name="teachers-list"),
    path("teacher/<int:pk>/", TeacherAPIView.as_view(), name="teacher-detail"),
]
