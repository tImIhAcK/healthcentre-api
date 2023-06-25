from rest_framework.permissions import BasePermission, SAFE_METHODS


class PatientPermission(BasePermission):
    methods = ("PUT", "PATCH", "DELETE")
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in self.methods:
            return True
        
        return False
    

class DoctorPermission(BasePermission):
    methods = ("PUT", "PATCH", "DELETE")
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in self.methods:
            return True
        
        return False

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            True
        return False
    def has_object_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return False