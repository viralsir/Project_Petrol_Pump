from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.
class creditor_master(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10,validators=[MinLengthValidator(10,"Phone numer must be of 10 digit")])
    officeno = models.CharField(max_length=7,validators=[MinLengthValidator(7,"Telephone numer must be of 10 digit")])
    contactpersonname = models.CharField(max_length=40)
    contactpersonmobile = models.IntegerField()
    companyname = models.CharField(max_length=30)
    homeno = models.IntegerField()
    street = models.CharField(max_length=20)
    area = models.CharField(max_length=30)
    pin = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    gstno = models.IntegerField()
    pendingbalance=models.IntegerField()
    creationdate = models.DateTimeField()
    def __str__(self):
        return f"vehicle({self.id})-diesel({self.fname})"
    def get_absolute_url(self):
        return reverse('creditor-view')