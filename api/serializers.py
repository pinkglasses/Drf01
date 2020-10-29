from django.conf import settings
from rest_framework import serializers

from api.models import Employee, Teacher


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.ImageField()
    pic = serializers.ImageField()

    aaa = serializers.SerializerMethodField()

    def get_aaa(self,obj):
        print(type(obj))
        return "aaa"

    gender = serializers.SerializerMethodField()
    def get_gender(self,obj):
        print(obj.get_gender_display())
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()
    def get_pic(self,obj):
        print(obj.pic)
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))

class EmployeeDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=3,
        min_length=2,
        error_messages={
            "max_length": "长度太长了",
            "min_length": "长度太短了",
        }

    )
    password = serializers.CharField()
    phone = serializers.CharField()

    def create(self, validated_data):
        print(self)
        print(validated_data)
        return Employee.objects.create(**validated_data)

class TeacherSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TeacherDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=3,
        min_length=2,
        error_messages={
            "max_length": "长度太长了",
            "min_length": "长度太短了",
        }

    )
    password = serializers.CharField()

    def create(self, validated_data):
        print(self)
        print(validated_data)
        return Teacher.objects.create(**validated_data)



