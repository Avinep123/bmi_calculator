# bmi/models.py
from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField()  # height in meters
    weight = models.FloatField()  # weight in kg
    bmi = models.FloatField(blank=True, null=True)
    bmi_classification = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        height_in_meters = self.height / 100  # Convert cm to meters if height is in cm
        self.bmi = self.weight / (height_in_meters ** 2)
        
        if self.bmi < 18.5:
            self.bmi_classification = 'Underweight'
        elif 18.5 <= self.bmi < 24.9:
            self.bmi_classification = 'Healthy'
        elif 25 <= self.bmi < 29.9:
            self.bmi_classification = 'Overweight'
        else:
            self.bmi_classification = 'Obesity'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
