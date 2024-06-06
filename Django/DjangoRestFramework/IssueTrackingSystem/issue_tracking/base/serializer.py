from rest_framework import serializers
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  
from django.forms.models import model_to_dict

from .models import *
import re


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'password2', 'date_joined', 'first_name', 'last_name',
                   'username', 'groups', 'phone', 'date_of_birth', 'gender',
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
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('password2', None)
        return super().update(instance, validated_data)
    



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField()

    def validate(self, data):
        print("-------------------------------------")
        password = data.get('password')
 
        if '@' in data.get('username'):
            email = data.get('username').lower()

            if not CustomUser.objects.filter(email = email).exists():
                raise serializers.ValidationError({'email':'email doesnot exists.'})
            
            user = CustomUser.objects.get(email = email)
            if user.password != password:
                raise serializers.ValidationError({'password':'Password not matched.'})
            if email and password:
                user = authenticate(email=email, password=password)
            data['username'] = email.lower()
        else:
            username = data.get('username').lower()
            if not CustomUser.objects.filter(username = username).exists():
                raise serializers.ValidationError({'username':'username doesnot exists.'})
            user = CustomUser.objects.get(username = username)
            # if user.password != password:
            #     raise serializers.ValidationError({'password':'Password not matched.'})
            if username and password:
                user = authenticate(username=username, password=password)
            data['username'] = username.lower()
        data['user'] = user
        return data
    


class TicketSerializer(serializers.ModelSerializer):
    created_user = serializers.SerializerMethodField()
    username = serializers.CharField(source='created_user.username', read_only=True)
    mr_title = serializers.CharField(source='title', required=False)


    class Meta:
        model = Ticket
        fields = '__all__'

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    def validate(self, validated_data):
        return validated_data
    
    # def get_mr_title(self, obj):
    #     return obj
    
    def create(self, validated_data):
        # print("-------------------------------------------------------------")
        # print(self.context.get('request').user.id)
        user = self.context.get('request').user
        if CustomUser.objects.get(id = user.id).groups.first() != Group.objects.get(name = "NormalUser"):
            raise serializers.ValidationError({"User": "Only Normal users can create Tickets."})
        if Ticket.objects.filter(title = validated_data['title'] ).exists():
            raise serializers.ValidationError({"title":"Title already exists."})
        if len(validated_data["assigned_to"]) == 0:
            validated_data["assigned_to"] = [Group.objects.get(name = "L1").id]
        print("-------------------------------------------------------------")
        print(validated_data)
        validated_data['created_user'] = user

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        print("------------------------------------------------")
        print(self.context.get('request'))
        user = self.context.get('request').user

        group = CustomUser.objects.get(id = user.id).groups.first().id
        print('------------------------------')
        print(validated_data, instance, user)
        if group != 4:
            if Ticket.objects.get(id=instance.id).assigned_to.first().id != group:
                raise serializers.ValidationError({"User":"Permission not granted."})
            if validated_data['status'] == 'Decline':
                validated_data['assigned_to'] = [Group.objects.get(name = "NormalUser").id]
            if validated_data['status'] == 'Forwarded':
                if group == Group.objects.get(name = "L1").id:
                    if 'assigned_to' not in validated_data:
                        validated_data['assigned_to'] = [Group.objects.get(name = "L2").id]
                elif group == Group.objects.get(name = "L2").id:
                    if 'assigned_to' not in validated_data:
                        validated_data['assigned_to'] = [Group.objects.get(name = "L3").id]
                else:
                    raise serializers.ValidationError({"User":"L3 user's cannot Forward."})
            elif validated_data['status'] == 'Resolved':
                if 'solved_by' not in validated_data:
                    validated_data['solved_by'] = user
            
        return super().update(instance, validated_data)
    
    def get_created_user(self, obj):
        # print(obj)
        # prof_obj = Profile.objects.get(user=User.objects.get(pk=obj.id))

        # user_ids = [i.id for i in obj.created_user]
        # users = CustomUser.objects.filter(id__in=user_ids)
        # serializer = UserSerializer(users, many=True)

        serializer = UserSerializer(CustomUser.objects.get(id = obj.created_user.id))
        # print("----------------------------------------------------")
        # print(serializer.data)
        return serializer.data
    

    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__" 

    def validate(self, attrs):
        return super().validate(attrs)   
    
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)




