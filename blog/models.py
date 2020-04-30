from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Compose(models.Model):
    to = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('blog-inbox')
