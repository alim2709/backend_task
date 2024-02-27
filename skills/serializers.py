from rest_framework import serializers

from skills.models import Skill
from topics.serializers import TopicListSerializer


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
            "description",
            "level",
            "topics",
        )


class SkillListSerializer(SkillSerializer):
    topics = TopicListSerializer(many=True, read_only=True)
