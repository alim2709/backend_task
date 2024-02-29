from rest_framework import viewsets

from skills.models import Skill
from skills.serializers import SkillSerializer, SkillListSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with skills"""

    queryset = Skill.objects.all().prefetch_related("topics__useful_links")
    serializer_class = SkillSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return SkillListSerializer
        return SkillSerializer
