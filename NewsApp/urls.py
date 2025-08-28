from django.urls import path
from .views import NewsAPIView, AllNewsAPIView

urlpatterns = [
    path("all_news/", AllNewsAPIView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsAPIView.as_view(), name="news-detail"),
]
