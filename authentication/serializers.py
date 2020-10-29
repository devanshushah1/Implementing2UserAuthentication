from rest_framework import serializers
from .models import User

class RegisterStudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_no', 'password']

        def validate(self, attrs):
            username = attrs.get('username', '')
            email = attrs.get('email', '')

            if not username.isalnum():
                raise serializers.ValidationError('Username should only contain alphanumeric charecters.')

            return attrs

        def create(self, validated_data):
            return User.objects.create_student(**validated_data)

class RegisterTeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_no', 'password']

        def validate(self, attrs):
            username = attrs.get('username', '')
            email = attrs.get('email', '')

            if not username.isalnum():
                raise serializers.ValidationError('Username should only contain alphanumeric charecters.')

            return attrs

        def create(self, validated_data):
            return User.objects.create_teacher(**validated_data)
