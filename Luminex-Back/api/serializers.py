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

    def create(self, validated_data):
           # Извлекаем и удаляем пароль из validated_data
           password = validated_data.pop('password', None)

           # Создаем пользователя без пароля
           user = super(CustomUserSerializer, self).create(validated_data)

           # Устанавливаем зашифрованный пароль
           if password:
               user.set_password(password)
               user.save()

           return user


class SkinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinType
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text','img']


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

class RatingSerializer(serializers.Serializer):
    testId = serializers.IntegerField()
    rating = serializers.IntegerField()