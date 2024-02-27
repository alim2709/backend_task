from django.shortcuts import render
from rest_framework import viewsets

from topics.models import Topic
from topics.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """Endpoint for CRUD operations with topics"""

    queryset = Topic.objects.all().prefetch_related("useful_links")
    serializer_class = TopicSerializer
