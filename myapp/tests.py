from django.test import TestCase
from .models import Student
# Create your tests here.

class StudentTest(TestCase):
    
   def setUp(self):
      Student.objects.create(name = 'monika',age=23, email = 'monika@gmail.com', address = 'Himachal pradesh')
      Student.objects.create(name = 'manmohan',age=23, email = 'monika@gmail.com', address = 'Himachal pradesh')
   
   def test_stu_find(self):

      monika  = Student.objects.get(name='monika')
      manmohan= Student.objects.get(name='monmohan')

   

      

