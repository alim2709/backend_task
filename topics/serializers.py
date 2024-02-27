from rest_framework import serializers

from topics.models import Topic, UsefulLink


class UsefulLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLink
        fields = ("id", "name", "link_url")


class TopicSerializer(serializers.ModelSerializer):
    useful_links = UsefulLinkSerializer(many=True, read_only=False)

    class Meta:
        model = Topic
        fields = ("id", "name", "description", "pet_project_ideas", "useful_links")

    def create(self, validated_data):
        useful_links_data = validated_data.pop("useful_links")

        topic = Topic.objects.create(**validated_data)
        for useful_link_data in useful_links_data:
            UsefulLink.objects.create(topic=topic, **useful_link_data)
        return topic
