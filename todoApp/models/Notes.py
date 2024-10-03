from api.models import BaseModel
from api.alias import AliasField
from django.db import models
from django.contrib.auth.models import User
from reversion import revisions as reversion


class Notes(BaseModel):
    """
    Table for notes
    """
    note_id = models.AutoField(db_column='ID', primary_key=True)
    note_title = models.TextField(db_column='TITLE', max_length=20)
    note_body = models.TextField(db_column='CONTENT', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = AliasField(db_column='TITLE', blank=True, null=True)

    class Meta:
       db_table = 'NOTES'
       app_label = 'todoApp'
       
reversion.register(Notes)