from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import authentication, permissions
from rest_framework.decorators import action

# Create your views here.

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class QuestioinsView(ModelViewSet):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(methods=["GET"], detail=False)
    def my_questions(self, request, *args, **kwargs):
        qs = request.user.questions_set.all()
        serializer = QuestionsSerializer(qs, many=True)
        return Response(data=serializer.data)

    
    @action(methods=["POST"], detail=True)
    def add_answer(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        question = Questions.objects.get(id=id)
        user = request.user

        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)