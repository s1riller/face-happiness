from djoser.serializers import UserSerializer
from rest_framework import serializers, generics
from .models import User, SkinType, Answer, UserTestResult, Medicine
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

class CustomUserSerializer(UserSerializer):
    birth_date = serializers.DateField()

    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name','birth_date')  # Добавьте поля, которые хотите запросить при регистрации


class SkinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinType
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class UserTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestResult
        fields = '__all__'


class UserTestResultListView(generics.ListCreateAPIView):
    queryset = UserTestResult.objects.all()
    serializer_class = UserTestResultSerializer


class UserResul(serializers.ModelSerializer):
    class Meta:
        model = UserTestResult
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'




