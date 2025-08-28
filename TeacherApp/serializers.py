from rest_framework import serializers
from .models import TeachersModel


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersModel
        fields = "__all__"
