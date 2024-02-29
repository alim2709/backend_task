from rest_framework import serializers

from professions.models import Profession
from skills.serializers import SkillListSerializer


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = (
            "id",
            "name",
            "description",
            "skills",
        )


class ProfessionListSerializer(ProfessionSerializer):
    skills = SkillListSerializer(many=True, read_only=True)
