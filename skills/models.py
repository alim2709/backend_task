from django.db import models

from topics.models import Topic


class Skill(models.Model):
    class LevelChoices(models.TextChoices):
        BEGINNER = "Beginner"
        INTERMEDIATE = "Intermediate"
        ADVANCED = "Advanced"

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    level = models.CharField(choices=LevelChoices, default="BEGINNER", max_length=255)
    topics = models.ManyToManyField(Topic, related_name="skills")

    def __str__(self):
        return self.name
