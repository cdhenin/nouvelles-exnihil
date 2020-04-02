import re
import html
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

MAX_CHAR_FOR_TRUNCATED_BIOGRAPHY = 500

def cleanhtml(text):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html.unescape(text))
    return cleantext

def get_excerpt(text):
    new_text = cleanhtml(text)
    return new_text[:500] + '...'

class Character(models.Model):
    name = models.CharField(max_length=200)
    biography = HTMLField()
    excerpt = models.TextField(max_length=500, blank=True, null=True)

    def to_dict(self):            
        return {
            'id': self.id,
            'name': self.name,
            'biography': self.biography,
            'excerpt': self.excerpt if self.excerpt else get_excerpt(self.biography),
            'novellas': self.novellas.values('title', 'id', 'excerpt', 'tags', 'created_at'),
        }
