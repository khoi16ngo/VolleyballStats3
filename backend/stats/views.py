from rest_framework import viewsets
from .models import Action
from .serializers import ActionSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer