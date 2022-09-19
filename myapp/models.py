from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Mname=models.CharField(max_length=40)
    Contact_no=models.CharField(max_length=10)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=10)
    Address_no=models.CharField(max_length=400)
    Added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
class Gallery(models.Model):
    image=models.ImageField(upload_to="media/%Y/%m/%d")
    description=models.TextField(max_length=300)
    Added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "Gallery"
class Tour(models.Model):
    tour_name=models.CharField(max_length=100)
    tour_image=models.ImageField(upload_to="media/%Y/%m/%d")
    place_from=models.CharField(max_length=100)
    place_to=models.CharField(max_length=100)
    places_to_be=models.TextField(max_length=500)
    days=models.IntegerField()
    nights=models.IntegerField()
    fare=models.FloatField()
    tour_descriptions=models.TextField(max_length="5000")

    def __str__(self):
        return self.tour_name
class Booking(models.Model):
    tour=models.ForeignKey(Tour,on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    From_date = models.DateField()
    Persons=models.IntegerField()
    Amount=models.FloatField()
    Payment_Method = models.CharField(max_length=100,default="online")
    Payment_status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
class Tourist(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    Fname=models.CharField(max_length=40)
    Lname=models.CharField(max_length=30)
    Contact_no=models.CharField(max_length=10)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=10)
    def __str__(self):
        return str(self.booking.id)



