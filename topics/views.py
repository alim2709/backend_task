from rest_framework import viewsets

from topics.models import Topic
from topics.serializers import TopicSerializer, TopicListSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with topics"""

    queryset = Topic.objects.all().prefetch_related("useful_links")
    serializer_class = TopicSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TopicListSerializer
        return TopicSerializer
