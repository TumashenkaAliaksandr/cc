from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # Здесь указываются имена ваших URL-шаблонов, например:
        return ['index', 'company', 'success']

    def location(self, item):
        return reverse(item)
