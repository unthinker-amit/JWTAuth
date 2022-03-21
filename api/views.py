import imp
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer   
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]   



