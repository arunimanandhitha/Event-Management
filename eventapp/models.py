from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="event_images")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="event_sub_images")

    def _str_(self):
        return f"{self.event.name} - Sub Photo"

class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.cus_name}" - {self.event.name}


