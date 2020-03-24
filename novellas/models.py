from tinymce.models import HTMLField
from django.db import models
from characters.models import Character

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Novella(models.Model):
    title = models.CharField(max_length=200)
    text = HTMLField()
    summary = HTMLField()
    characters = models.ManyToManyField(Character, verbose_name="list of characters", related_name="novellas")
    tags = models.ManyToManyField(Tag, verbose_name="list of tags")
    created_at = models.DateTimeField('creation date')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'text': self.text,
            'created_at': self.created_at,
            'characters': self.characters.values('name', 'id', 'biography'),
            'tags': self.tags.values('name', 'id')
        }
