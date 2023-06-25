from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.forms import Textarea
from .models import Patient, Doctor, Prescription, Medicine


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'is_completed')
    list_filter = ('is_completed', 'doctor', 'patient')
    search_fields = ('doctor__first_name', 'doctor__last_name', 'patient__first_name', 'patient__last_name')
    # readonly_fields = ('time_started', 'updated_at')
    formfield_overrides = {
        JSONField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'level', 'gender', 'age', 'email')
    list_filter = ('level', 'gender')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    # readonly_fields = ('created_at', 'updated_at')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email')
    list_filter = ('specialization',)
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiry_date', 'available')
    list_filter = ('expiry_date', 'available')
    search_fields = ('name', 'expiry_date', 'available')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Medicine, MedicineAdmin)

