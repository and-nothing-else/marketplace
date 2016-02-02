from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail.fields import ImageField
from seo.models import SEOFieldsMixin


class ArticleManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class Article(SEOFieldsMixin, models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    slug = models.SlugField(_('slug'))
    title = models.CharField(_('title'), max_length=128)
    image = ImageField(_('image'), upload_to='articles', help_text=_('550x300px'))
    text = RichTextUploadingField(_('text'))
    active = models.BooleanField(_('active'), default=True)

    objects = ArticleManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('articles:article_detail', args=[str(self.slug)])

    def get_browser_title(self):
        return self.browser_title or self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('article')
        verbose_name_plural = _('articles')
