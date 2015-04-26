from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from cms_genome_browser.models import Browser

class BrowserListView(ListView):
    model = Browser
    template_name = 'cms_genome_browser/browser_list.html'
    context_object_name = 'browser_list'


class BrowserDetailView(DetailView):
    model = Browser
    template_name = 'cms_genome_browser/browser_detail.html'
    context_object_name = 'browser'
