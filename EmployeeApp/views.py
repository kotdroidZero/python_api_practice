from math import fabs
from django.shortcuts import render
from django.urls import is_valid_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Employee,Department
from EmployeeApp.serializers import EmployeeSerializer,DepartmentSerializer
# Create your views here.


@csrf_exempt
def departmentApi(request,id=0):
     if request.method == 'GET':
        departments = Department.objects.all()
        department_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(department_serializer.data,safe=False)
     elif request.method=='POST':
        departmentData = JSONParser().parse(request)
        departmentSerializer = DepartmentSerializer(data=departmentData)
        if departmentSerializer.is_valid():
            departmentSerializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
     elif request.method=='PUT':
        # convert coming json  to   model
        departmentData = JSONParser().parse(request)
        #get data from db
        data = Department.objects.get(DepartmentId = departmentData['DepartmentId'])
        department_serializer = DepartmentSerializer(data,data=departmentData)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Updated Succesfully',safe=False)
        return JsonResponse("Failed to update",safe=False) 
     elif request.method=='DELETE':
        departmentData = Department.objects.get(DepartmentId = id)
        departmentData.delete()
        return JsonResponse("Deleted Succesfullly",safe=False)







