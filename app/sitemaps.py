from django.contrib.sitemaps import Sitemap
from novellas.models import Novella
from characters.models import Character
from django.urls import reverse

class NovellaSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Novella.objects.all()

    def lastmod(self, obj):
        return obj.created_at
        
    def location(self,obj):
        return '/novellas/%s' % (obj.id)

class CharacterSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Character.objects.all()

    def lastmod(self, obj):
        return min(list(obj.novellas.values_list('created_at', flat=True)))
         
    def location(self,obj):
        return '/characters/%s' % (obj.id)

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['novellas:index', 'characters:index', 'home', 'about', 'lexiconItems:index']

    def location(self, item):
        return reverse(item)