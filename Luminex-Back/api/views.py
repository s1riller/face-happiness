from django.shortcuts import render
from rest_framework import generics, parsers, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import SkinType, Question, Answer, UserTestResult, Medicine
from .resource import MedicineResource
from .serializers import *

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
            'birth_date': user.birth_date,  # Добавляем идентификатор пользователя
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
        }
        return Response(data)

    def put(self, request):
        user = request.user
        data = request.data

        # Обновляем данные пользователя, если они предоставлены в запросе
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.birth_date = data.get('birth_date', user.birth_date)

        # Сохраняем изменения
        user.save()

        return Response({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birth_date': user.birth_date,
        }, status=status.HTTP_200_OK)

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

class CustomUserCreateView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateRecomendationView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateRecomendationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            test_id = serializer.validated_data['testId']
            rating = serializer.validated_data['rating']

            try:
                test_result = UserTestResult.objects.get(id=test_id)
            except UserTestResult.DoesNotExist:
                return Response({'message': 'Test result not found'}, status=status.HTTP_404_NOT_FOUND)

            test_result.rate = rating
            test_result.save()

            # Сериализуем объект test_result и отправляем его в ответе
            serialized_test_result = UserTestResultSerializer(test_result)

            return Response({'message': 'Rating saved successfully', 'test_result': serialized_test_result.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
