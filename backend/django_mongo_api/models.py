from django.db import models

# Create your models here.    
class Test(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    content = models.CharField(max_length=200,blank=False, default='')
    
    class Meta:
        db_table = 'test'