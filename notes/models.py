from django.db import models

# Create your models here.

class Note(models.Model):
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.id}"
