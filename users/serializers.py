from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

# from quiz.serializers import QuestionSerializer
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number',
                  'email', 'date_joined', 'password', 'password2', 'score']


        def validate(self, attrs):
            if attrs['password'] != attrs ['password']:
                raise serializers.ValidationError(
                    {"password: password fields don't match"}
                )


class UserProfileSerializer(serializers.ModelSerializer):
    # questions = QuestionSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'date_joined']