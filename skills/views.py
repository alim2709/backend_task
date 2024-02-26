from rest_framework import viewsets

from skills.models import Skill
from skills.serializers import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with skills"""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
