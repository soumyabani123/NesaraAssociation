from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class member(models.Model):
    member_id=models.IntegerField(primary_key=True)
    member_name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    phone_no=models.IntegerField(default=False)
    site_no=models.IntegerField(default=False)
    def __str__(self):
        return self.member_name
    class Meta:
        db_table="NesaraAssociation_member"
    
    
class meeting(models.Model):
    date=models.DateField(auto_now=False)
    time=models.TimeField(auto_now=False)
    host=models.CharField(max_length=30)
    def __str__(self):
        return self.host

