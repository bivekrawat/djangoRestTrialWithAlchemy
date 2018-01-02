from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from .models import employee
from .serializers import employeesSerializer


class employeeList(APIView):
    def get(self, request):
        employees1 = employee.objects.all()
        serializer = employeesSerializer(employees1, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        pass
