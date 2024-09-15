from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
       
        if request.method == 'DELETE':
            return request.user.is_staff 
        if request.method == 'GET':
            return False 
        return True 
     