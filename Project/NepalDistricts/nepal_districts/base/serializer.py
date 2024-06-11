from rest_framework import serializers
from .models import *

class MuncipalitySerializer(serializers.ModelSerializer):
    # district_id = serializers.SerializerMethodField(read_only=True)
    # province_id = serializers.SerializerMethodField(read_only=True)
    url = serializers.CharField(source = 'get_absolute_url', read_only=True)

    class Meta:
        model = Muncipality
        fields = '__all__'

    # def get_district_id(self, obj):
    #     return DistrictSerializer(District.objects.get(id=obj.district_id.id)).data
    
    # def get_province_id(self, obj):
    #     return ProvinceSerializer(Province.objects.get(id=obj.province_id.id)).data
    



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

