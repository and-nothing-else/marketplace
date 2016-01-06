"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'marketplace.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'marketplace.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for marketplace.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.ModelList(
            title="Платные услуги",
            models=[
                'tariff.models.Tariff',
                'order.models.Order',
            ]
        ))

        self.children.append(modules.Group(
            title="Администрирование сайта",
            display="tabs",
            children=[
                modules.ModelList(
                    title="Пользователи",
                    models=[
                        'user.models.MarketplaceUser',
                        'profile.models.Shop',
                    ]
                ),
                modules.ModelList(
                    title="Справочники",
                    models=[
                        'dictionary.models.Region',
                    ]
                ),
                modules.AppList(
                    title='Все приложения',
                    # exclude=('django.contrib.*',)
                )
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for marketplace.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
