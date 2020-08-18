from django.db import models
from django.utils import timezone

class text_input(models.Model):
    text = models.CharField(max_length=80)

    def __str__(self):
        return self.text