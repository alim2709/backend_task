from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

from skills.models import Skill
from skills.serializers import SkillListSerializer, SkillSerializer
from topics.models import Topic
from topics.tests.test_topics_api import sample_useful_link

SKILL_URL = reverse("skills:skill-list")


def detail_url(skill_id):
    return reverse("skills:skill-detail", args=[skill_id])


def sample_skill(**params):
    topic_with_useful_link_1 = sample_useful_link()
    topic_with_useful_link_2 = sample_useful_link(name="name_test2")
    topic_1 = Topic.objects.get(id=topic_with_useful_link_1.topic.id)
    topic_2 = Topic.objects.get(id=topic_with_useful_link_2.topic.id)
    defaults = {
        "name": "test_name",
        "description": "test_description",
        "level": "BEGINNER",
    }
    defaults.update(params)
    skill = Skill.objects.create(**defaults)
    skill.topics.set([topic_1, topic_2])

    return skill


class SkillApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.skill_1 = sample_skill()
        self.skill_2 = sample_skill(name="test_name_22")

    def test_list_skills(self):
        res = self.client.get(SKILL_URL)

        skills = Skill.objects.all()

        serializer = SkillListSerializer(skills, many=True)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data["results"], serializer.data)

    def test_detail_skill(self):

        skill = sample_skill()

        url = detail_url(skill_id=skill.id)
        res = self.client.get(url)

        serializer = SkillSerializer(skill, many=False)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    def test_create_skill(self):
        topic_with_usefullink = sample_useful_link()
        topic = Topic.objects.get(id=topic_with_usefullink.topic.id)

        skill_payload = {
            "name": "test_skill",
            "description": "test_description",
            "topics": [
                topic.id,
            ],
        }
        res = self.client.post(SKILL_URL, skill_payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_skill(self):
        skill = self.skill_1
        skill_payload = {
            "name": "updated_name",
            "description": "updated_description",
        }
        url = detail_url(skill.id)
        res = self.client.patch(url, skill_payload)
        skill.refresh_from_db()
        serializer = SkillSerializer(skill, many=False)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_delete_skill(self):
        skill = self.skill_1
        url = detail_url(skill.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Skill.objects.filter(id=skill.id).exists())
