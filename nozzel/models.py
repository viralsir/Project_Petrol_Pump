from django.db import models
from django.urls import reverse
# Create your models here.
class nozzel_master(models.Model):
    choices=[("petrol","petrol"),("diesel","diesel")]

    nozzel_no=models.CharField(max_length=30)
    type=models.CharField(choices=choices,default='petrol',max_length=30)
    remark=models.CharField(max_length=30)

    def __str__(self):
        return f"nozzel_no({self.nozzel_no})-type({self.type})"

    def get_absolute_url(self):
        return reverse('nozzel-view')
