from django.db import models


class UsefulLink(models.Model):
    name = models.CharField(max_length=255)
    link_url = models.URLField()
    topic = models.ForeignKey(
        "Topic", on_delete=models.CASCADE, related_name="useful_links"
    )

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pet_project_ideas = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Topic: {self.name}"
