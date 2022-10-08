from rest_framework import serializers
from account.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True, write_only = True)
    password2 = serializers.CharField(required = True, write_only = True)
    class Meta:
        model = CustomUser
        fields = ["first_name" , "last_name" , "username" , "email" , "password" , "password2" , "is_superuser"]
    def create(self, validated_data):
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")
        password2 = validated_data.get("password2")
        is_superuser = validated_data.get("is_superuser")

        if password == password2:
            user = User(first_name=first_name, last_name=last_name,username=username,email=email,is_superuser=is_superuser)
            user.set_password(password)
            user.save()
            return user

        else:
            return serializers.ValidationError({
                "error": "Both password do not match"
            })

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True, write_only = True)
    password2 = serializers.CharField(required = True, write_only = True)
    class Meta:
        model = CustomUser
        fields = ["first_name" , "last_name" , "username" , "email" , "password" , "password2"]
    def create(self, validated_data):
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password == password2:
            user = User(first_name=first_name, last_name=last_name,username=username,email=email)
            user.set_password(password)
            user.save()
            return user

        else:
            return serializers.ValidationError({
                "error": "Both password do not match"
            })
