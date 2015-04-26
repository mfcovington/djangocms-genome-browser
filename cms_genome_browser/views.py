from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from cms_genome_browser.models import Browser

class BrowserListView(ListView):
    model = Browser
    template_name = 'cms_genome_browser/browser_list.html'
    context_object_name = 'browser_list'

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar:

            menu = self.request.toolbar.get_or_create_menu('genome-browsers-menu', 'Genome Browsers')

            url_change = reverse('admin:cms_genome_browser_browser_changelist')
            url_addnew = reverse('admin:cms_genome_browser_browser_add')
            menu.add_sideframe_item('Edit Genome Browsers', url=url_change)
            menu.add_modal_item('Add New Genome Browser', url=url_addnew)
            menu.add_break()

            url_change = reverse('admin:cms_genome_browser_track_changelist')
            url_addnew = reverse('admin:cms_genome_browser_track_add')
            menu.add_sideframe_item('Edit Tracks', url=url_change)
            menu.add_modal_item('Add New Track', url=url_addnew)
            menu.add_break()

            url_change = reverse('admin:cms_genome_browser_stylesheet_changelist')
            url_addnew = reverse('admin:cms_genome_browser_stylesheet_add')
            menu.add_sideframe_item('Edit Stylesheets', url=url_change)
            menu.add_modal_item('Add New Stylesheet', url=url_addnew)
            menu.add_break()

            url_change = reverse('admin:cms_genome_browser_species_changelist')
            url_addnew = reverse('admin:cms_genome_browser_species_add')
            menu.add_sideframe_item('Edit Species', url=url_change)
            menu.add_modal_item('Add New Species', url=url_addnew)
            menu.add_break()

            url_change = reverse('admin:cms_genome_browser_coordsystem_changelist')
            url_addnew = reverse('admin:cms_genome_browser_coordsystem_add')
            menu.add_sideframe_item('Edit Coordinate Systems', url=url_change)
            menu.add_modal_item('Add New Coordinate System', url=url_addnew)

        return super(BrowserListView, self).render_to_response(context, **response_kwargs)


class BrowserDetailView(DetailView):
    model = Browser
    template_name = 'cms_genome_browser/browser_detail.html'
    context_object_name = 'browser'

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar:

            menu = self.request.toolbar.get_or_create_menu('genome-browsers-detail-menu', self.object.name)

            url_change = reverse('admin:cms_genome_browser_browser_change', args=[self.object.id])
            url_delete = reverse('admin:cms_genome_browser_browser_delete', args=[self.object.id])
            menu.add_modal_item('Edit %s' % self.object.name, url=url_change)
            menu.add_modal_item('Delete %s' % self.object.name, url=url_delete)
            menu.add_break()

            url_change = reverse('admin:cms_genome_browser_browser_changelist')
            url_addnew = reverse('admin:cms_genome_browser_browser_add')
            menu.add_sideframe_item('Edit Genome Browsers', url=url_change)
            menu.add_modal_item('Add New Genome Browser', url=url_addnew)

        return super(BrowserDetailView, self).render_to_response(context, **response_kwargs)
