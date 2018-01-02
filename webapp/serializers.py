from rest_framework import serializers
from .models import employee


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        # fields = ('fName', 'lName')
        fields = '__all__'
