from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import RegisterStudentSerializer, RegisterTeacherSerializer
from .models import User
from .utils import Util

# Create your views here.
class RegisterStudentView(generics.GenericAPIView):
    serializer_class = RegisterStudentSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        # user.is_student = True
        # user.save()
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://' + current_site + relativeLink + '?token=' + str(token)
        email_subject = 'Verify your email'
        email_body = 'Hi ' + user.username + 'Please click on the following link to verify your account \n.' + absurl
        data = {'email_subject':email_subject, 'email_body':email_body, 'to_email':user.email}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)

class RegisterTeacherView(generics.GenericAPIView):
    serializer_class = RegisterTeacherSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        user.is_teacher = True
        user.save()
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://' + current_site + relativeLink + '?token=' + str(token)
        email_subject = 'Verify your email'
        email_body = 'Hi ' + user.username + 'Please click on the following link to verify your account \n.' + absurl
        data = {'email_subject':email_subject, 'email_body':email_body, 'to_email':user.email}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    pass