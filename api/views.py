from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer      



