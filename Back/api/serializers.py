from djoser.serializers import UserSerializer
from rest_framework import serializers, generics
from .models import User, SkinType, Answer, UserTestResult, Medicine
from djoser.serializers import UserCreateSerializer


class CustomUserSerializer(UserSerializer):
    birth_date = serializers.DateField()

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ('birth_date',)


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

