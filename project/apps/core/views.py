from rest_framework import viewsets
from .models import Keyvalue
from .serializers import KeyvalueSerializer


class KeyvalueViewSet(viewsets.ModelViewSet):
    queryset = Keyvalue.objects.all()
    serializer_class = KeyvalueSerializer

