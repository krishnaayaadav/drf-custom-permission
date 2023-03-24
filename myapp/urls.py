from django.urls import path,include
from .views import RegisterationView,HomePage,UpdateView,DetailView

# student apis-endpoints
from .api_views import StudentAPI, StudentViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('student-api', viewset=StudentViewSet, basename='students')


urlpatterns = [
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('student-registeration/', RegisterationView.as_view(), name='stu_registertion'),
    path('student-updation/<int:id>/', UpdateView.as_view(), name='stu_updation'),
    path('student-details/<int:id>/', DetailView.as_view(), name='detials_page'),

    # api-endpoints
    # path("", include(routers.urls))
    path('student-api/',StudentAPI.as_view(), name='student_api'),


]
