from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    published_date = models.DateTimeField(blank=True, null=True)
    boast = models.BooleanField(default=True)
    roast = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} - {self.author}"
