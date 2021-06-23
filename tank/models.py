from django.db import models
from django.urls import reverse

# Create your models here.
class tank_master(models.Model):
    date=models.DateField()
    petrolbefore=models.FloatField()
    dieselbefore=models.FloatField()
    petrolafter = models.FloatField(null=True,blank=True)
    dieselafter = models.FloatField(null=True,blank=True)
    lostpetrol = models.FloatField(null=True,blank=True)
    lostdiesel = models.FloatField(null=True,blank=True)
    lostpetrolprice = models.FloatField(null=True,blank=True)
    lostdieselprice = models.FloatField(null=True,blank=True)

    def __str__(self):
        return f"petrol({self.lostpetrol})-diesel({self.lostdiesel})"

    def get_absolute_url(self):
        return reverse('Tank-view')