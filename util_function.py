from django.utils import timezone
from django.conf import settings
from main_app.models import Unit

def extra_context ( context, title ):
    context['current_year'] = timezone.now().year
    context['app_name'] = settings.APP_NAME
    context['support_email'] = settings.SUPPORT_EMAIL
    context['support_phone'] = settings.SUPPORT_PHONE
    context['title'] = title
    
    return context


def extra_context_index ( context, title ):
    context['current_year'] = timezone.now().year
    context['app_name'] = settings.APP_NAME
    context['support_email'] = settings.SUPPORT_EMAIL
    context['support_phone'] = settings.SUPPORT_PHONE
    context['title'] = title
    context['montreal_listings_count'] = Unit.objects.filter(location__city__iexact='Montreal').order_by('date_created').count()
    context['toronto_listings_count'] = Unit.objects.filter(location__city__iexact='Toronto').order_by('date_created').count()
    context['vancouver_listings_count'] = Unit.objects.filter(location__city__iexact='Vancouver').order_by('date_created').count()
    context['ottawa_listings_count'] = Unit.objects.filter(location__city__iexact='Ottawa').order_by('date_created').count()
    
    return context