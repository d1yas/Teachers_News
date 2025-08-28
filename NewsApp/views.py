from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import NewsModel
from .serializers import NewsSerializer
from .pagination import NewsPagination


class AllNewsAPIView(APIView):
    def get(self, request):
        news = NewsModel.objects.all().order_by("-id") 
        paginator = NewsPagination()
        paginated_news = paginator.paginate_queryset(news, request)
        serializer = NewsSerializer(paginated_news, many=True)

        return paginator.get_paginated_response(serializer.data)


class NewsAPIView(APIView):
    def get(self, request, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
