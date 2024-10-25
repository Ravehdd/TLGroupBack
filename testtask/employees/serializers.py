from rest_framework import serializers
from .models import *


class IndexSerializer(serializers.ModelSerializer):
    subdivision = serializers.CharField(source='subdivision.subdiv_name')
    role = serializers.CharField(source='role.role_name')

    class Meta:
        model = Employees
        fields = ("id", "full_name", "salary", "subdivision", "subdivision_id", "role", "role_id", "hiring_date")
