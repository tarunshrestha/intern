from rest_framework import serializers
from .models import *

# class SnippetSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=False, max_length = 100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices =STYLES_CHOICES, default = 'friendly')

#     def created(self, validate_data):
#         return Snippet.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.title = validate_data.get('title', instance.title)
#         instance.code = validate_data.get('code', instance.code)
#         instance.linenos = validate_data.get('linenos', instance.linenos)
#         instance.language = validate_data.get('language', instance.language)
#         instance.style = validate_data.get('style', instance.style)
#         instance.save()
#         return instance

## ---------------------------------------------------------------------
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style'] 