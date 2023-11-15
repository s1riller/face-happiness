from django.shortcuts import render
from rest_framework import generics, parsers, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import SkinType, Question, Answer, UserTestResult, Medicine
from .resource import MedicineResource
from .serializers import SkinTypeSerializer, AnswerSerializer, UserTestResultSerializer, MedicineSerializer

from .utils import get_medicines_for_user


# Create your views here.
def profile_view(request):
    return render(request, 'api/profile.html')


class SkinTypeList(generics.ListCreateAPIView):
    queryset = SkinType.objects.all()
    serializer_class = SkinTypeSerializer


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'id': user.id,  # Добавляем идентификатор пользователя
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
        }
        return Response(data)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        data = []
        for question in questions:
            answers = Answer.objects.filter(question=question)
            serializer = AnswerSerializer(answers, many=True)
            data.append({
                'id': question.id,
                'question': question.text,
                'answers': serializer.data
            })
        return Response(data)


class UserTestResultView(APIView):
    def post(self, request, format=None):
        serializer = UserTestResultSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class getResult(APIView):
#     def get(self, request):
#


class MedicineListView(generics.ListAPIView):
    serializer_class = MedicineSerializer

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):

        medicines = Medicine.objects.all()
        return medicines


class UserTestResultList(generics.ListAPIView):
    serializer_class = UserTestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        # Получите объекты UserTestResult текущего пользователя (по токену доступа)
        user = self.request.user
        return UserTestResult.objects.filter(user=user.id)


class UserTestResultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTestResult.objects.all()
    serializer_class = UserTestResultSerializer


