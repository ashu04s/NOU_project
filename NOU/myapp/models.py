from django.db import models
from datetime import timezone

# Create your models here.
class tbl_session(models.Model):
    id =models.IntegerField(primary_key=True,auto_created=True)
    session_name=models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    strt_date=models.DateField()
    end_date=models.DateField()
    Dor=models.DateField(auto_now_add=True)
    