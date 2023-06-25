from django import forms
from .models import Patient, Prescription, Doctor

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'level', 'gender', 'age', 'email', 'phone_number', 'address', 'prescription']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['symptoms', 'prescription', 'doctor', 'patient', 'medicine', 'time_started', 'drug_usage_duration', 'is_completed']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'specialization', 'prescription']
