from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200)
    biography = HTMLField()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'biography': self.biography,
            'novellas': self.novellas.values('title', 'id', 'summary', 'tags', 'created_at'),
        }
