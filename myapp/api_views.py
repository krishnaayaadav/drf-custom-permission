from .models import Student
from .serializers import StudentSerializer

# rest-framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# auth class and permission
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import permissions

# custom permissions
from .custom_permission import HasAuthorPermission

# import view-sets
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):

   authentication_classes = [BasicAuthentication]
   permission_classes     = [permissions.AllowAny]

   def list(self, request):
      stus = Student.objects.all()
      serializer = StudentSerializer(stus, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
   
   def retrieve(self, request, pk=None):
      try:
         stu = Student.objects.get(pk=pk)
      except:
         pass
      else:
         serialiser = StudentSerializer(stu)
         return Response(serialiser.data, status=status.HTTP_200_OK)
      
      return Response(status=status.HTTP_400_BAD_REQUEST)
   




class StudentAPI(APIView):

   authentication_classes = [SessionAuthentication]
   permission_classes     = [HasAuthorPermission]
   
   def get(self, request, format=None):
      """Get method for hanling get requests """
      id  = request.data.get('id', None)

      if not id: # if id does exist or none
         all_stus = Student.objects.all()
         serializer = StudentSerializer(all_stus, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
      else:
         try:
            stu = Student.objects.get(pk=id)
         except Student.DoesNotExist:
            res = {'DoesNotExist': f'Student Does Not Exist With This Id: {id}'}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
         else:
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
      
   def post(self, request, format=None):
      """Post method handling to provide funcnality to insert data using api"""

      serializer = StudentSerializer(data=request.data)

      if serializer.is_valid():
         serializer.save()
         res = {'Created Successfuly': 'Congrats Data created/inserted successfuly', 'data':serializer.data}

         return Response(res, status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors)
      
   def patch(self, request, format=None):
      """PATCH: request for partialy updating the data"""

      id  = request.data.get('id', None)

      if id is not None: # means id does exist
        try:
            stu = Student.objects.get(pk=id)
        except:
           error = {'Error': f'Student not found with this id: {id} '}
           return Response(error, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
               serializer.save()
               res  = {'Updated Successfuly!': 'Congrats Data Successfuly Updated', 'data': serializer.data}
               return Response(res, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         
      return Response(status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, format=None):
      """Delete request here"""
      id  = request.data.get('id', None)

      if id is not None:
         try:
            stu = Student.objects.get(pk=id)
         except:
            pass
         else:
            stu.delete()
            msg = {'Deleted successfuly': 'Data deleted successfuly'}
            return Response(msg, status=status.HTTP_200_OK)
      
      error = {'Invalid request': 'Requested method is not valid'}
         
      return Response(error, status=status.HTTP_400_BAD_REQUEST)
