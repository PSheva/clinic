from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator


SERVICE_CHOICES = (
    ("Check review", "Check review"),
    ("Planed treatment", "Planed treatment"),
    ("Teeth cleaning", "Teeth cleaning"),
    
    )
TIME_CHOICES = (
    
         ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),    
    ("9 AM", "9 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10 AM", "10 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 AM", "12 AM"),
    ("13:30 AM", "13:30 AM"),
    ("14 AM", "14 AM"),
    ("15:30 AM", "15:30 AM"))


# TIME_CHOICES = (
    
#          ("3 PM", "3 PM"),
#     ("3:30 PM", "3:30 PM"),
#     ("4 PM", "4 PM"),
#     ("4:30 PM", "4:30 PM"),
#     ("5 PM", "5 PM"),
#     ("5:30 PM", "5:30 PM"),
#     ("6 PM", "6 PM"),
#     ("6:30 PM", "6:30 PM"),
#     ("7 PM", "7 PM"),
#     ("7:30 PM", "7:30 PM"))
    
   
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    specialisation = models.CharField(max_length=100)
    rating = models.FloatField(default = 0.0, validators=[MaxValueValidator(5.0)])
    
    def __str__(self):
        return f"{self.name} |  {self.surname} | specialisation: {self.specialisation}"

    def get_absolute_url(self):
        return reverse('doctor-info', kwargs={'pk': self.pk})

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Check review")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    # doctor = models.CharField(default = 'Suhodolia' ,max_length = 100) #  ,choices = DOCTOR_CHOICES
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
    



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

