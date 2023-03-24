from rest_framework.permissions import BasePermission



class HasAuthorPermission(BasePermission):
    
   def has_permission(self, request, view):

      user = request.user

      if request.method == 'POST':
         # if user has change permission than only insert data
         user.has_perm("myapp.add_student")

         return True
      
      # permission for update data for particular user only
      if request.method == 'PATCH':
         user.has_perm("myapp.change_student")
         return True

      # permisssion for delete operation of specific user only
      if request.method == 'DELETE':
         user.has_perm("myapp.delete_student")
         return True
      
      return False