from django.db import models

class input_text(models.Model):
    text = models.CharField(max_length=80)

    def __str__(self):
        return self.text