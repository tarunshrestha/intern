from rest_framework import serializers
from django.template.defaultfilters import slugify
from .models import *
import re


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = '__all__'
        # exculde = ['created_at']
        # fields = ['title', 'description']

    def validate(self, validated_data):
        if validated_data.get('title'):
            title = validated_data['title']
            regex=re.compile('[@_!#$%^&*()<>?|\/}{~:;]')
            if (regex.search(title)!=None):
                raise serializers.ValidationError('Title cannot contain special charecters.')
        return validated_data
    
    def get_slug(self,obj):
        return slugify(obj.title)
