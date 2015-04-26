from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class BrowserApp(CMSApp):
    name = _("Genome Browser App")
    urls = ["cms_genome_browser.urls"]
    app_name = "cms_genome_browser"

apphook_pool.register(BrowserApp)
