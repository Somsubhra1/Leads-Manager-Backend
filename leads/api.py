from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead ViewSet
# A view set gives crud based api service without explicitly writing routes for all methods
class LeadViewSet(viewsets.ModelViewSet):
    # queryset = Lead.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadSerializer

    # Changing queryset to display just the leads of authenticated user
    def get_queryset(self):
        return super().request.user.leads.all()

    # Adding owner property to request body data
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
