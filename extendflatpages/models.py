from django.utils.translation import ugettext_lazy as _
from seo.models import SEOFieldsMixin
from django.contrib.flatpages.models import FlatPage


class ExtendFlatpage(SEOFieldsMixin, FlatPage):

    def get_browser_title(self):
        return self.browser_title or self.title

    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
