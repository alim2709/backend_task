from rest_framework import viewsets

from professions.models import Profession
from professions.serializers import ProfessionSerializer, ProfessionListSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with professions"""

    queryset = Profession.objects.all().prefetch_related("skills__topics__useful_links")
    serializer_class = ProfessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProfessionListSerializer
        return ProfessionSerializer
