from rest_framework import serializers
from .models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ["id", "name", "roll_no", "city"]
