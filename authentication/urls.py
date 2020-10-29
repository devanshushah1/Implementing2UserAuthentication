from django.urls import path
from . import views


urlpatterns = [
    path('register/student/', views.RegisterStudentView.as_view(), name='register-student'),
    path('register/teacher/', views.RegisterTeacherView.as_view(), name='register-teacher'),
    path('email-verify/', views.VerifyEmail.as_view(), name='email-verify'),
]