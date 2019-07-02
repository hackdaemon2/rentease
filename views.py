from django.views.generic import (TemplateView, DetailView, ListView)
from django.views import View
from main_app.util_function import extra_context, extra_context_index
from main_app.models import Unit

# Create your views here.
class AboutUsView ( TemplateView ):
    template_name = 'main_app/about_us.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'About Us' )
    
    

class UnitDetailView ( DetailView ):
    template_name = 'main_app/unit_detail.html'
    context_object_name = 'unit_list'
    model = Unit
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Apartment Detail' )
        

class SearchView ( View ):
    def get ( self, request, *args, **kwargs ):
        self.post( request, *args, **kwargs )
    
    def post ( self, request, *args, **kwargs ):
        pass



class ContactUsView ( TemplateView ):
    template_name = 'main_app/contact_us.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Contact Us' )



class VendorView ( TemplateView ):
    template_name = 'main_app/contact_us.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Vendor' )



class IndexView ( TemplateView ):
    template_name = 'main_app/index.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context_index ( context, 'Home' )



class FAQView ( TemplateView ):
    template_name = 'main_app/faq.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'FAQ' )



class FindARoomMateView ( TemplateView ):
    template_name = 'main_app/find_a_roommate.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Find A Roommate' )


class MovingServiceView ( TemplateView ):
    template_name = 'main_app/moving_service.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Moving Service' )



class CleaningServiceView ( TemplateView ):
    template_name = 'main_app/cleaning_service.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Cleaning Service' )



class DashboardView ( TemplateView ):
    template_name = 'main_app/dashboard.html'
    
    def get_context_data ( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        return extra_context ( context, 'Dashboard' )