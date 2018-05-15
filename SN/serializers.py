from rest_framework import serializers
from .models import SNUser, Post
from django.contrib.auth.hashers import make_password


class SNUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SNUser
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'gender', 'birth_date', 'location', 'is_staff', 'is_superuser', 'is_active',  'date_joined', 'last_login']

    def create(self, validated_data):
        user = SNUser.objects.create(
        email=validated_data['email'],
        username=validated_data['username'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        password=make_password(validated_data['password']),
        gender = validated_data['gender'],
        birth_date=validated_data['birth_date'],
        location = validated_data['location']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'owner', 'text', 'date']

