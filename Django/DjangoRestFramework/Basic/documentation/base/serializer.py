from rest_framework import serializers
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  
from .models import *
import re


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    # texts = serializers.SerializerMethodField()
    # requests = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = '__all__'
        # exculde = ['created_at']
        # fields = ['title', 'description','slug', 'texts', 'title_and_des']

    def validate(self, validated_data):
        if validated_data.get('title'):
            title = validated_data['title']
            regex=re.compile('[@_!#$%^&*()<>?|}{~:;]')
            if (regex.search(title)!=None):
                raise serializers.ValidationError('Title cannot contain special charecters.')
        return validated_data
    
    def get_slug(self,obj):
        return slugify(obj.title)
    
    # def get_requests(self, instance):
    #     return instance.response
    
    # def get_texts(self, obj):
    #     return obj.title + ' ' + str(obj.is_done)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ['id', 'password', 'date_joined', 'first_name', 'last_name', 'username', 'address', 'phone', 'date_of_birth', 'profile_picture', 'gender', 'email', 'is_verified', 'otp']
        # exculde = ['is_superuser', 'is_staff', 'user_permissions',]

    def validate(self, data):
        data['gender'] = int(data['gender']) 
        # data['password'] = make_password(data['password'])
        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    # class Meta:
    #     model = CustomUser
    #     fields = ['id', 'email', 'password']


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        # password = make_password(password)
        if not CustomUser.objects.filter(email = email).exists():
            raise serializers.ValidationError('Email doesnot exists.')
        user = CustomUser.objects.get(email = email)
        if user.password != password:
            raise serializers.ValidationError('Password not matched.')
        if email and password:
            user = authenticate(email=email, password=password)
                                    
            # user = authenticate(request=self.context.get('request'),
            #                     email=email, password=password)

        data['user'] = user     
        return data

class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

