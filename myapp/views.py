from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.views import View
from django.contrib import messages

# Create your views here.

class HomePage(View):
   def get(self, request):
      all_stu = Student.objects.all()
      context = {
         'all_students': all_stu
      }
      return render(request, 'myapp/home.html', context)

class RegisterationView(View):
    
   def get(self, request):
      form = StudentForm()
      context = {
         'form': form
      }
      return render(request, 'myapp/register2.html', context)

   def post(self, request):

      form = StudentForm(request.POST)

      if form.is_valid(): # chekcing weather form is valid or not
         
         name = form.cleaned_data['name']
         age  = form.cleaned_data['age']
         email = form.cleaned_data['email']
         address = form.cleaned_data['address']
         # stu  = Student(name=name, age=age, email=email, address=address)
         # stu.save()

         form.save()
         messages.success(request, 'Congrats! Data Successfuly Inserted')
         return redirect('homepage')
         


      else:
         context = {
            'form': form
         }
         return render(request, 'myapp/register2.html',context)
    
class UpdateView(View):

   def get(self, request, id=None):
      homepage = redirect('homepage')

      try:
         if not id: # if id is None No id provided by user
            return redirect('homepage')
         else:  # if id is not None

            if(type(id) ==int):
               try:
                  stu = Student.objects.get(pk=id)

               except Student.DoesNotExist:
                  messages.error(request, f'Student Does Not Exists With This id: {id} ')
                  res =  redirect('homepage')

               except:
                  res =  redirect('homepage')

               else:
                  form = StudentForm(instance=stu)
                  context = {
                     'form': form
                  }
                  res = render(request, 'myapp/update.html', context)
               
               finally:
                  return res
            else:
               return homepage
      except:
         return homepage

   def post(self, request, id=None):
      homepage =  redirect('homepage')
      try:
         if not id: # if id is none
            return homepage
         
         elif(type(id) == int):      
                    # If id is not None
                    # now id exist ok
            try:
               stu = Student.objects.get(pk=id)

            except Student.DoesNotExist:
               messages.error(request, 'Student Does Not Exist With This Id')
               return homepage
            
            except:
               return homepage
            
            else:
               form = StudentForm(request.POST,instance=stu)


               if form.is_valid():
                  form.save()
                  messages.success(request, 'Cograts! Data Successfuly Updated!')
                  return homepage
               else:
                  return render(request, 'myapp/update.html', {'form': form})
        
         else:
            return homepage
      except:
         return homepage


class DetailView(View):

   def get(self, request, id=None):

      if id is not None:

         try:
            stu = Student.objects.get(pk=id)
         except:
            return redirect('homepage')
         
         else:
            return render(request, 'myapp/details_page.html',{'stu': stu} )
      return redirect('homepage')