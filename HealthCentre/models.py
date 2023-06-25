import json
from django.db import models
from django.db.models import JSONField
from phonenumber_field.modelfields import PhoneNumberField
import os
from datetime import timezone

LEVEL_CHOICES = (
    ('100', '100'),
    ('200', '200'),
    ('300', '300'),
    ('400', '400'),
    ('500', '500'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

file_path = os.path.join(os.path.dirname(__file__), 'specializations.json')
SPECIALIZATION_CHOICES = [(spec, spec) for spec in json.load(open(file_path))]

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=256)
    prescription = models.CharField(max_length=256, blank=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_patient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('first_name',)


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES)
    patients = models.ManyToManyField('Patient', related_name='pateint_doctor')
    prescription = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('first_name',)


class Prescription(models.Model):
    symptoms = models.TextField(max_length=2000, default='')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medicine = models.ManyToManyField('Medicine', related_name='medicine')
    time_started = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.doctor} - {self.patient}\n\nPrescription: {self.prescription}'

class Medicine(models.Model):
    name = models.CharField(max_length=250)
    expiry_date = models.DateField(default=timezone)
    available = models.BooleanField(default=False)
    consumption = JSONField(default=dict)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return f'{self.name}'
    