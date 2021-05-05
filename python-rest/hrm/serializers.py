from rest_framework import serializers
from hrm.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class DeptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dept
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
