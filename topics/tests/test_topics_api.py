from django.urls import reverse

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from topics.models import Topic, UsefulLink
from topics.serializers import TopicListSerializer, TopicSerializer

TOPIC_URL = reverse("topics:topic-list")


def detail_url(topic_id):
    return reverse("topics:topic-detail", args=[topic_id])


def sample_topic(**params):
    defaults = {
        "name": "test_name",
        "description": "test_description",
        "pet_project_ideas": "test_pet_project_ideas",
    }
    defaults.update(params)

    return Topic.objects.create(**defaults)


def sample_useful_link(**params):
    topic = sample_topic()
    defaults = {"name": "test_link", "link_url": "test.com", "topic": topic}
    defaults.update(params)

    return UsefulLink.objects.create(**defaults)


class TopicApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.topic_with_useful_link_1 = sample_useful_link()
        self.topic_with_useful_link_2 = sample_useful_link()

    def test_list_topics(self):
        res = self.client.get(TOPIC_URL)
        topics = Topic.objects.all()
        serializer = TopicListSerializer(topics, many=True)
        print(serializer.data)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data["results"], serializer.data)

    def test_detail_topic(self):
        topic_with_useful_link = self.topic_with_useful_link_1
        topic_id = topic_with_useful_link.topic.id

        topic = Topic.objects.get(id=topic_id)
        url = detail_url(topic_id)

        res = self.client.get(url)
        serializer = TopicSerializer(topic, many=False)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    def test_create_topic_with_useful_link(self):
        payload = {
            "name": "TEST_Data Science",
            "description": "Test_Description",
            "pet_project_ideas": "test_pet",
            "useful_links": [
                {"name": "test1111", "link_url": "https://www.test.com/"},
                {"name": "Towards_test2", "link_url": "https://toward.com/"},
            ],
        }
        serializer = TopicSerializer(data=payload)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(serializer.data, payload)

    def test_update_topic_with_useful_link(self):
        topic_with_useful_link = self.topic_with_useful_link_1
        topic_id = topic_with_useful_link.topic.id

        payload = {
            "name": "Updated Topic",
            "description": "Updated Description",
            "pet_project_ideas": "Updated Pet Project Ideas",
            "useful_links": [
                {"name": "Updated Link 1", "link_url": "https://www.updatedlink1.com/"},
                {"name": "Updated Link 2", "link_url": "https://www.updatedlink2.com/"},
            ],
        }

        url = detail_url(topic_id)
        res = self.client.patch(url, payload)
        topic = Topic.objects.get(id=topic_id)
        serializer = TopicSerializer(topic, many=False)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    def test_delete_topic_with_useful_link(self):
        topic_with_useful_link = self.topic_with_useful_link_1
        topic_id = topic_with_useful_link.topic.id

        url = detail_url(topic_id)
        res = self.client.delete(url)

        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Topic.objects.filter(id=topic_id).exists())
