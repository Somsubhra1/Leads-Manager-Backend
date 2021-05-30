from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead ViewSet
# A view set gives crud based api service without explicitly writing routes for all methods
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
