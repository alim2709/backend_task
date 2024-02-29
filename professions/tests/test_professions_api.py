from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from professions.models import Profession
from professions.serializers import ProfessionListSerializer, ProfessionSerializer
from skills.tests.test_skills_api import sample_skill

PROFESSION_URL = reverse("professions:profession-list")


def detail_url(profession_id):
    return reverse("professions:profession-detail", args=[profession_id])


def sample_profession(**params):
    skill_1 = sample_skill()
    skill_2 = sample_skill(name="skill2323")

    defaults = {
        "name": "Sample Profession",
        "description": "Sample description",
    }
    defaults.update(params)
    profession = Profession.objects.create(**defaults)
    profession.skills.set([skill_1, skill_2])

    return profession


class ProfessionApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.profession1 = sample_profession()
        self.profession2 = sample_profession(name="test_name_22")

    def test_list_professions(self):
        res = self.client.get(PROFESSION_URL)

        professions = Profession.objects.all()

        serializer = ProfessionListSerializer(professions, many=True)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data["results"], serializer.data)

    def test_create_profession(self):
        skill_1 = sample_skill(name="skill1")
        skill_2 = sample_skill(name="skill2")

        payload = {
            "name": "New Profession",
            "description": "New profession description",
            "skills": [skill_1.id, skill_2.id],
        }
        res = self.client.post(PROFESSION_URL, payload)

        profession = Profession.objects.get(id=res.data["id"])
        serializer = ProfessionSerializer(profession, many=False)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, serializer.data)

    def test_update_profession(self):
        payload = {
            "name": "Updated Profession",
            "description": "Updated profession description",
        }
        url = detail_url(self.profession1.id)
        res = self.client.patch(url, payload)

        self.profession1.refresh_from_db()
        serializer = ProfessionSerializer(self.profession1)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_delete_profession(self):
        url = detail_url(self.profession1.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Profession.objects.filter(id=self.profession1.id).exists())
