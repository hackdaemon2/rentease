from django.db import models
from django.conf import settings

# Create your models here.
class Conversation ( models.Model ):
    title = models.CharField ( max_length = 255, blank = True )
    creator = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    date_updated = models.DateTimeField ( auto_now = True, editable = True )
    date_deleted = models.DateTimeField ( auto_now = True, editable = False )
    
    class Meta:
        db_table = 'conversations_tbl'



class Participant ( models.Model ):
    user = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    conversation = models.ForeignKey ( to = Conversation, on_delete = models.CASCADE )
    
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    
    class Meta:
        db_table = 'participants_tbl'
        
        
        
class Message ( models.Model ):
    message_data = models.CharField ( max_length = 255, blank = False )
    conversation = models.ForeignKey ( to = Conversation, on_delete = models.CASCADE )
    sender = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    is_read = models.BooleanField ( default = False )
    
    date_created = models.DateTimeField ( auto_now_add = True, editable = False )
    date_deleted = models.DateTimeField ( auto_now = True, editable = False )
    
    class Meta:
        db_table = 'messages_tbl'



class DeletedMessage ( models.Model ):
    message = models.ForeignKey ( to = Message, on_delete = models.CASCADE )
    user = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    
    date_created = models.DateTimeField ( auto_now = True, editable = False )
    
    class Meta:
        db_table = 'deleted_messages_tbl'



class DeletedConversation ( models.Model ):
    conversation = models.ForeignKey ( to = Conversation, on_delete = models.CASCADE )
    user = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    
    date_created = models.DateTimeField ( auto_now = True, editable = False )
    
    class Meta:
        db_table = 'deleted_conversations_tbl'



class BlockList ( models.Model ):
    user = models.ForeignKey ( to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    participant = models.ForeignKey ( to = Participant, on_delete = models.CASCADE )
    
    date_created = models.DateTimeField ( auto_now = True, editable = False )
    
    class Meta:
        db_table = 'blocklist_tbl'