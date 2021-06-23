from django.db import models

from django.urls import reverse


# Create your models here.

class employee(models.Model):

    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.IntegerField()
    telephone = models.IntegerField()
    block=models.CharField(max_length=10)
    street=models.CharField(max_length=20)
    area=models.CharField(max_length=30)
    pin=models.IntegerField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    dob = models.DateField()
    op=[("Male","Male"),("Female","Female")]
    gender = models.CharField(max_length=10,choices=op)
    education = models.CharField(max_length=30)
    dateofjoin = models.DateField()
    choices = [("Morning", "Morning"), ("Noon", "Noon"),("Night","Night")]
    shifttime = models.CharField(choices=choices,max_length=10)
    workinghours = models.IntegerField()
    salary = models.IntegerField()
    bankname = models.CharField(max_length=30)
    bankaccountno = models.IntegerField()
    IFSCcode = models.IntegerField()
    panno = models.IntegerField()
    aadharno = models.IntegerField()
    reference = models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos',blank=True)
    document=models.FileField(upload_to='documents')

    def __str__(self):
        return f"employee({self.id})-diesel({self.name})"

    def get_absolute_url(self):
        return reverse('employee-view')





