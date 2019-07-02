from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Location ( models.Model ):
    city = models.CharField ( max_length = 255, blank = True )
    province = models.CharField ( max_length = 255, blank = True )
    country = models.CharField ( max_length = 255, blank = True, default = 'canada' )
    
    class Meta:
        db_table = 'location_tbl'
        
        
        
class UnitStatus ( models.Model ):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'
    UNIT_STATUS = (
        ( AVAILABLE, 'Available' ),
        ( UNAVAILABLE, 'Unavailable' ),
    )
    
    status = models.CharField ( max_length = 255, blank = False, choices = UNIT_STATUS, default = AVAILABLE )
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    
    class Meta:
        db_table = 'unit_status_tbl'
        


class Unit ( models.Model ):
    CONDO = 'C'
    SUITE = 'S'
    UNIT_TYPE = (
        ( CONDO, 'Condo' ),
        ( SUITE, 'Suite' ),
    )
    
    unit_status = models.ForeignKey ( to = UnitStatus, on_delete = models.CASCADE )
    number_of_rooms = models.PositiveIntegerField ( default = 1, blank = False )
    unit_type = models.CharField ( max_length = 255, choices = UNIT_TYPE, default = CONDO )
    number_of_bathrooms = models.PositiveIntegerField ( default = 1 )
    has_den = models.BooleanField ( default = False )
    price = models.DecimalField ( decimal_places = 2, max_digits = 15, default = 0 )
    short_title = models.CharField ( max_length = 255, blank = True )
    description = models.TextField ( max_length = 512 )
    location = models.ForeignKey( to = Location, on_delete = models.CASCADE )
    address = models.CharField ( max_length = 255, blank = True )
    area_sq_ft = models.DecimalField ( max_digits = 10, decimal_places = 2, default = 0 )
    date_created = models.DateTimeField( auto_now_add = True, editable = False )
    date_updated = models.DateTimeField( auto_now = True, editable = True )
    
    class Meta:
        db_table = 'units_tbl'
    
    def __str__ ( self ):
        self.get_fullname()
            
    def get_absolute_url ( self ):
        return reverse ( 'main_app:unit_details', kwargs = { 'pk' : self.id } )
    
    

class Image ( models.Model ):
    image = models.ImageField ( upload_to = 'media/apartments/' )
    unit = models.ForeignKey ( to = Unit, on_delete = models.CASCADE, null = True )
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    date_updated = models.DateTimeField ( auto_now = True, editable = True )   
    
    class Meta:
        db_table = 'unit_images_tbl'
    
    def __str__ ( self ):
        return self.__class__ ( )
    
        
        
class UnitSavedSearch ( models.Model ):
    user = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    unit = models.ForeignKey ( to = Unit, on_delete = models.CASCADE )
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )

    class Meta:
        db_table = 'unit_saved_search_tbl'
        unique_together = ( ( 'user', 'unit' ), )



class ApplicationStatus ( models.Model ):
    name = models.CharField ( max_length = 255, blank = False )
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    
    class Meta:
        db_table = 'application_status_tbl'



class ApplicationInfo ( models.Model ):
    unit = models.ForeignKey ( to = Unit, on_delete = models.CASCADE )
    location = models.ForeignKey ( to = Location, on_delete = models.CASCADE )
    user = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    application_status = models.ForeignKey ( to = ApplicationStatus, on_delete = models.CASCADE )
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    
    class Meta:
        db_table = 'application_info_tbl'
        



