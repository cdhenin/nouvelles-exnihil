from django.db import models

class LexiconItem(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField()
    created_at = models.DateTimeField('creation date')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'definition': self.definition,
            'created_at': self.created_at,
        }
