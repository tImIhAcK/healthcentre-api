from rest_framework import generics
from .models import Patient, Doctor, Prescription, Medicine
from .serializers import PatientSerializer, DoctorSerializer, PrescriptionSerializer, MedicineSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from permissions.permission import PatientPermission, DoctorPermission, ReadOnly


class PatientListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
class PrescriptionListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    

class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class MedicineListCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    

class MedicineDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
