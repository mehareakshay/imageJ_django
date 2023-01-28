from django.db import models

# Create your models here.

class Admin_login(models.Model):
    username = models.CharField(max_length=300,null=False)
    password=models.CharField(max_length=300,null=False)

    class Meta:
        db_table = 'admin'
        
class Chemical_Properties(models.Model):
    chemical_category = models.CharField(max_length=200, null=False, default=None)
    chemical_name = models.CharField(max_length=200, null=False, default=None)
    value_b = models.CharField(max_length=200, null=False, default=None)
    value_m = models.CharField(max_length=200, null=False, default=None)
    parameter_y = models.CharField(max_length=200, null=False, default=None)

    class Meta:
        db_table = 'chemical_properties'