from rest_framework import serializers
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  
from .models import *
import re


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'password2', 'date_joined', 'first_name', 'last_name',
                   'username', 'groups', 'phone', 'date_of_birth', 'profile_picture', 'gender',
                     'email', 'is_verified', 'otp', 'company']

    def validate(self, data):
        password = data['password']
        print(data)
        if  data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Passwords doesnot match.'})
        if len(password) < 8 :
            raise serializers.ValidationError({'password': 'Password must have more then 8 charecters.'})
        print(data)
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        if "groups" not in validated_data:
            validated_data["groups"] = [4]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('password2', None)
        return super().update(instance, validated_data)
    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not CustomUser.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email':'Email doesnot exists.'})
        user = CustomUser.objects.get(email = email)
        if user.password != password:
            raise serializers.ValidationError({'password':'Password not matched.'})
        if email and password:
            user = authenticate(email=email, password=password)
        data['email'] = email.lower()
        data['user'] = user
        return data
    


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


    def validate(self, validated_data):
        return validated_data
    
    def create(self, validated_data):
        if CustomUser.objects.get(id = validated_data["id"]).groups != [4]:
            raise serializers.ValidationError({"User": "Only Normal users can create Tickets."})
        if Ticket.objects.filter(title = validated_data['title'] ).exists():
            raise serializers.ValidationError({"title":"Title already exists."})
        if "assigned_to" not in validated_data:
            validated_data["assigned_to"] = [1]
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        group = CustomUser.objects.get(id = validated_data["recent_user"].id).groups.first().id
        # print('------------------------------')
        # print(validated_data, instance)
        if group != 4:
            if Ticket.objects.get(id=instance.id).assigned_to.first().id != group:
                raise serializers.ValidationError({"User":"Permission not granted."})
            if validated_data['status'] == 'Forwarded':
                if group == 1:
                    if 'assigned_to' not in validated_data:
                        validated_data['assigned_to'] = [2]
                elif group == 2:
                    if 'assigned_to' not in validated_data:
                        validated_data['assigned_to'] = [3]
                else:
                    raise serializers.ValidationError({"User":"L3 user's cannot Forward."})
            elif validated_data['status'] == 'Resolved':
                if 'solved_by' not in validated_data:
                    validated_data['solved_by'] = validated_data['recent_user']
            
        return super().update(instance, validated_data)
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__" 

    def validate(self, attrs):
        return super().validate(attrs)   
    
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)




