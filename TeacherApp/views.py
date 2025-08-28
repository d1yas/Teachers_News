from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TeachersModel
from .serializers import TeacherSerializer
from .pagination import TeacherPagination


class All_TeacherListAPIView(APIView):
    def get(self, request):
        teachers = TeachersModel.objects.all().order_by("id")

        paginator = TeacherPagination()
        paginated_teachers = paginator.paginate_queryset(teachers, request)
        serializer = TeacherSerializer(paginated_teachers, many=True)

        return paginator.get_paginated_response(serializer.data)


class TeacherAPIView(APIView):
    def get(self, request, pk):
        teacher = get_object_or_404(TeachersModel, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
