"""rentease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from main_app import views

app_name = 'main_app'
urlpatterns = [
    # general view url mapping
    path('', views.IndexView.as_view(), name = 'home'),
    path('about_us', views.AboutUsView.as_view(), name = 'about_us'),
    path('contact_us', views.ContactUsView.as_view(), name = 'contact_us'),
    path('faq', views.FAQView.as_view(), name = 'faq'),
    path('find_roommate', views.FindARoomMateView.as_view(), name = 'find_roommate'),
    path('moving_service', views.MovingServiceView.as_view(), name = 'moving_service'),
    path('cleaning_service', views.CleaningServiceView.as_view(), name = 'cleaning_service'),
    path('vendor', views.VendorView.as_view(), name = 'vendor'),
    path('apartments/<int:pk>', views.UnitDetailView.as_view(), name = 'unit_details'),
    path('search', views.SearchView.as_view(), name = 'search'),
    
    # dahsboard view url mapping
    path('dashboard', views.DashboardView.as_view(), name = 'dashboard'),
    
]
