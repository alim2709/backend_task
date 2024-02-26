from rest_framework import viewsets

from professions.models import Profession
from professions.serializers import ProfessionSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with professions"""

    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
