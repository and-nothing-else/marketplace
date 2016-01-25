from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import SEOFile

SEO_ADMIN_FIELDSET = (_('SEO'), {
    'fields': ('browser_title', 'meta_description'),
    'classes': ('collapse',)
})

admin.site.register(SEOFile)
