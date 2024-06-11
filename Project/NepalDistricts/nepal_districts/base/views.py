from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, APIView

from .models import * 
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from nepali_municipalities import NepalMunicipality
import openpyxl
# from xlsx2 import xlsx2pdf
# Create your views here.
def index(request):
    nep = NepalMunicipality()
    districts = nep.all_districts()
    municipalities = NepalMunicipality('Syangja').all_municipalities()
    muncipality_info = NepalMunicipality().all_data_info("Arjunchaupari")

    print(muncipality_info)
    print("----------------------------------------")
    print(municipalities)
    # breakpoint()
    return HttpResponse("Test")


class MunicipalityApi(viewsets.ModelViewSet):
    queryset = Muncipality.objects.all()
    serializer_class = MuncipalitySerializer
    # lookup_field = 'pk'



def add_districts(request):
    districts = District.objects.all()
    for district in districts:
        municipalities = NepalMunicipality(f'{district}').all_municipalities()
        for i in range(len(municipalities)):
            print(municipalities[i])
            municipalitie = NepalMunicipality().all_data_info(f'{municipalities[i]}') # all muncipalities
            mun = Muncipality.objects.filter(name = municipalitie[0]['name'])
            if not mun.exists():
                province = Province.objects.get_or_create(name =municipalitie[0]['province'])
                data = Muncipality.objects.create(name=municipalitie[0]['name'] ,province_id=province[0], district_id=district)
                data.save()
                print(data)
    return HttpResponse("Completed")


def export_data(request):
    queryset = Muncipality.objects.all()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Nepal Districts'
    headers = ['ID', 'Name', 'District', 'Province', 'Country']
    sheet.append(headers)
    for data in queryset:
        row = [
            data.id, 
            data.name, 
            data.district_id.name, 
            data.province_id.name, 
            data.country_id.name
        ]
        sheet.append(row)
    # workbook.save('nepal_districts.xlsx')

    workbook.save('nepal_districts.csv')
    pdf = 'nepal_districts.pdf'


    return HttpResponse("Excel file has been created successfully.")


