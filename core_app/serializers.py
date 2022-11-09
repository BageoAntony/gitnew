from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrations
        fields = "__all__"


class QuestionsSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model = Questions
        fields = [
            "title",
            "describtion",
            "image",
            "user",
        ]
    
class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    created_date = serializers.CharField(read_only=True)
    class Meta:
        model = Answers
        fields = [
            "question",
            "answer",
            "user",
            "created_date"
        ]