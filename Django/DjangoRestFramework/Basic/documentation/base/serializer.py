from rest_framework import serializers
from django.template.defaultfilters import slugify
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
            regex=re.compile('[@_!#$%^&*()<>?|\/}{~:;]')
            if (regex.search(title)!=None):
                raise serializers.ValidationError('Title cannot contain special charecters.')
        return validated_data
    
    def get_slug(self,obj):
        return slugify(obj.title)
    
    # def get_requests(self, instance):
    #     return instance.response
    
    # def get_texts(self, obj):
    #     return obj.title + ' ' + str(obj.is_done)
