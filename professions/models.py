from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    skills = models.ManyToManyField("Skill", related_name="professions")

    def __str__(self):
        return self.name
