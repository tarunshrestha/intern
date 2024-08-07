from rest_framework import serializers
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  
from .models import *
import re
from rest_framework.validators import UniqueTogetherValidator


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    # texts = serializers.SerializerMethodField()
    # requests = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = '__all__'
        # validators = [UniqueTogetherValidator(queryset = Todo.objects.all(), fields = ['title', 'description'])]
        # extra_kwargs = { 'title': {"required":True}}
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
    # a = serializers.
    # tryEmail = serializers.CharField(max_length = 255)
    # i = serializers.PrimaryKeyRelatedField
    # texts = serializers.SerializerMethodField()
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ['id', 'password', 'password2', 'date_joined', 'first_name', 'last_name', 'username', 'address', 'phone', 'date_of_birth', 'profile_picture', 'gender', 'email', 'is_verified', 'otp']
        # exculde = ['is_superuser', 'is_staff', 'user_permissions',]

    def validate(self, data):
        password = data['password']
        print(data)
        if  data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Passwords doesnot match.'})
        if len(password) < 8 :
            raise serializers.ValidationError({'password': 'Password must have more then 8 charecters.'})
        # print(data['gender'])
        # data['gender'] = int(data['gender']) 
        # data['profile_picture'] = '/mnt/824EB9CC4EB9B96D/RealSoftHR/intern/Django/DjangoRestFramework/Basic/documentation' + data['profile_picture']
        # if data['username'].lower() == 'amar':
        #     raise serializers.ValidationError({'username':'Amar is blocked.'})
        # data['password'] = make_password(data['password'])
        # data.pop('password2', None)
        print(data)
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        # validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('password2', None)
        # if 'password' in validated_data:
            # validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    # class Meta:
    #     model = CustomUser
    #     fields = ['id', 'email', 'password']


    def validate(self, data):
        # email = data.get('email')
        # password = data.get('password')
        # # password = make_password(password)
        # # password = make_password(password)
        # if not CustomUser.objects.filter(email = email).exists():
        #     raise serializers.ValidationError({'email':'Email doesnot exists.'})
        # user = CustomUser.objects.get(email = email)
        # # if user.password != password:
        # #     raise serializers.ValidationError({'password':'Password not matched.'})
        # if email and password:
        #     user = authenticate(email=email, password=password)
        #     if not user:
        #         breakpoint()
        #         raise serializers.ValidationError({'password':'Password not matched.'})

        #     # user = authenticate(request=self.context.get('request'),
        #     #                     email=email, password=password)

        email = data.get('email')
        password = data.get('password')

        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email does not exist.'})
        user = CustomUser.objects.get(email=email)

        # user = authenticate(email=email, password=password)
        
        if password != user.password:
            raise serializers.ValidationError({'password': 'Password is incorrect.'})

        data['email'] = email.lower()
        data['user'] = user
        return data

class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


