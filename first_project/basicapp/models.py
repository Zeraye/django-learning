from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.title
