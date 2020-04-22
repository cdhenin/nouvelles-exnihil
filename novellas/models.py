import re
import html
from django.utils.timezone import now
from tinymce.models import HTMLField
from django.db import models
from characters.models import Character

def cleanhtml(text):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html.unescape(text))
    return cleantext

def get_excerpt(text):
    new_text = cleanhtml(text)
    return new_text[:500] + '...'

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Novella(models.Model):
    title = models.CharField(max_length=200)
    text = HTMLField()
    excerpt = models.TextField(max_length=500, null=True, blank=True)
    characters = models.ManyToManyField(Character, verbose_name="list of characters", related_name="novellas")
    tags = models.ManyToManyField(Tag, verbose_name="list of tags")
    created_at = models.DateTimeField('creation date', default=now, blank=True)

    def to_dict(self, short=False):
        if(short == True):
            return {
                'id': self.id,
                'title': self.title,
                'excerpt': self.excerpt if self.excerpt else get_excerpt(self.text),
                'created_at': self.created_at,
                'tags': self.tags.values('name', 'id')
            }
        return {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt if self.excerpt else get_excerpt(self.text),
            'text': self.text,
            'created_at': self.created_at,
            'characters': [character.to_dict() for character in self.characters.all()],
            'tags': self.tags.values('name', 'id')
        }
