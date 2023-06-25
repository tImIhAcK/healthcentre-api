from django.urls import path
from .views import (
    PatientDetailView, PatientListCreateView,
    DoctorDetailView, DoctorListCreateView,
    PrescriptionDetailView, PrescriptionListCreateView,
    MedicineDetailView, MedicineListCreateView    
)

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('prescriptions/', PrescriptionListCreateView.as_view(), name='prescription-list'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('medicines/', MedicineListCreateView.as_view(), name='medicine-list'),
    path('medicines/<int:pk>/', MedicineDetailView.as_view(), name='medicine-detail'),
]
