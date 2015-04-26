from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from cms_genome_browser.menu import BrowsersMenu

class BrowserApp(CMSApp):
    name = _("Genome Browser App")
    urls = ["cms_genome_browser.urls"]
    app_name = "cms_genome_browser"
    menus = [BrowsersMenu]

apphook_pool.register(BrowserApp)
