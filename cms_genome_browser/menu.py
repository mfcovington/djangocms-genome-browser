from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from cms_genome_browser.models import Browser

class BrowsersMenu(CMSAttachMenu):
    name = _("Genome Browsers Menu")

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for browser in Browser.objects.all():
            node = NavigationNode(
                browser.name,
                reverse('cms_genome_browser:browser_detail', args=(browser.slug,)),
                browser.slug
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(BrowsersMenu)
