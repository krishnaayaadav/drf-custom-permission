from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    """Student Form to perform registeration, updation fields name, email, age and address"""
    class Meta:
        model  = Student
        fields = ('name', 'age', 'email', 'address')

