from django.contrib.sitemaps import Sitemap
from .models import Set

class SetSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Set.can_use.all()
    
    def lastmod(self, obj):
        return obj.updated 