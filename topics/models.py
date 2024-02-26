from django.db import models


class UsefulLink(models.Model):
    name = models.CharField(max_length=255)
    link_url = models.URLField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pet_project_ideas = models.CharField(max_length=255)
    useful_links = models.ForeignKey(
        UsefulLink, on_delete=models.CASCADE, null=True, related_name="topics"
    )

    def __str__(self) -> str:
        return f"Topic: {self.name}"
