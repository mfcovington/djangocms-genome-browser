from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class BrowserToolbar(CMSToolbar):

    def populate(self):

        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER, _('Apps')
        )

        position = admin_menu.get_alphabetical_insert_position(
            _('Genome Browsers'),
            SubMenu
        )

        if not position:
            position = admin_menu.find_first(
                Break,
                identifier=ADMINISTRATION_BREAK
            ) + 1
            admin_menu.add_break('custom-break', position=position)

        genome_browsers_menu = admin_menu.get_or_create_menu(
            'genome-browsers-menu',
            _('Genome Browsers ...'),
            position=position
        )

        url_change = reverse('admin:cms_genome_browser_browser_changelist')
        url_addnew = reverse('admin:cms_genome_browser_browser_add')
        genome_browsers_menu.add_sideframe_item(_('Edit Genome Browsers'), url=url_change)
        genome_browsers_menu.add_modal_item(_('Add New Genome Browser'), url=url_addnew)
        genome_browsers_menu.add_break()

        url_change = reverse('admin:cms_genome_browser_track_changelist')
        url_addnew = reverse('admin:cms_genome_browser_track_add')
        genome_browsers_menu.add_sideframe_item('Edit Tracks', url=url_change)
        genome_browsers_menu.add_modal_item('Add New Track', url=url_addnew)
        genome_browsers_menu.add_break()

        url_change = reverse('admin:cms_genome_browser_stylesheet_changelist')
        url_addnew = reverse('admin:cms_genome_browser_stylesheet_add')
        genome_browsers_menu.add_sideframe_item('Edit Stylesheets', url=url_change)
        genome_browsers_menu.add_modal_item('Add New Stylesheet', url=url_addnew)
        genome_browsers_menu.add_break()

        url_change = reverse('admin:cms_genome_browser_species_changelist')
        url_addnew = reverse('admin:cms_genome_browser_species_add')
        genome_browsers_menu.add_sideframe_item('Edit Species', url=url_change)
        genome_browsers_menu.add_modal_item('Add New Species', url=url_addnew)
        genome_browsers_menu.add_break()

        url_change = reverse('admin:cms_genome_browser_coordsystem_changelist')
        url_addnew = reverse('admin:cms_genome_browser_coordsystem_add')
        genome_browsers_menu.add_sideframe_item('Edit Coordinate Systems', url=url_change)
        genome_browsers_menu.add_modal_item('Add New Coordinate System', url=url_addnew)
