from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from django.utils.decorators import method_decorator

from api.models import Student, Employee, Teacher
from api.serializers import EmployeeSerializer, EmployeeDeSerializer, TeacherSerializer, TeacherDeSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self,request,*args,**kwargs):
        print("get Success")
        username = request.GET.get("username")
        print(username)
        return HttpResponse("GET ok")

    def post(self,request,*args,**kwargs):
        print("post Success")
        username = request.POST.get("username")
        print(username)
        return HttpResponse("post ok")

class StudentAPIView(APIView):

    renderer_classes = (JSONRenderer,)
    def get(self,request,*args,**kwargs):
        print("get Success")
        print(request.GET.get("email"))

        stu_id = kwargs.get("id")
        stu_obj = Student.objects.get(pk=stu_id)
        print(stu_obj)

        return Response("GET ok")

    def post(self,request,*args,**kwargs):
        print("post Success")
        return Response("post ok")

class EmployeeAPIView(APIView):

    def get(self,request,*args,**kwargs):
        emp_id =kwargs.get("id")

        if emp_id:
            emp_obj = Employee.objects.get(pk = emp_id)
            employee_serializer = EmployeeSerializer(emp_obj).data
            print()
            return Response({
                "status": 200,
                "message": "查询单个员工成功",
                "results": employee_serializer
            })
        else:
            employee_object_all = Employee.objects.all()
            emp_data = EmployeeSerializer(employee_object_all,many=True).data
            print(emp_data)
            return Response({
                "status": 200,
                "message": "查询多个员工成功",
                "results": emp_data
            })

    def post(self,request,*args,**kwargs):
            request_data = request.data

            if not isinstance(request_data,dict)or request_data=={}:
                return Response({
                    "status": 400,
                    "message": "参数有误",
                })
            serializer = EmployeeDeSerializer(data=request_data)

            if serializer.is_valid():
                # 调用save()方法进行数据的保存  必须重写create()方法
                emp_ser = serializer.save()
                print(emp_ser)
                return Response({
                    "status": 200,
                    "message": "员工添加成功",
                    "results": EmployeeSerializer(emp_ser).data
                })
            else:

                return Response({
                    "status": 400,
                    "message": "员工添加失败",
                    # 保存失败的信息会包含在 .errors中
                    "results": serializer.errors
                })

class TeacherAPIView(APIView):

    def get(self,request,*args,**kwargs):
        teacher_id =kwargs.get("id")

        if teacher_id:
            teacher_obj = Teacher.objects.get(pk = teacher_id)
            teacher_serializer = TeacherSerializer(teacher_obj).data
            return Response({
                "status": 200,
                "message": "查询单个老师成功",
                "results": teacher_serializer
            })
        else:
            teacher_object_all = Teacher.objects.all()
            teacher_data = TeacherSerializer(teacher_object_all,many=True).data
            return Response({
                "status": 200,
                "message": "查询多个员工成功",
                "results": teacher_data
            })

    def post(self,request,*args,**kwargs):
            request_data = request.data

            if not isinstance(request_data,dict)or request_data=={}:
                return Response({
                    "status": 400,
                    "message": "参数有误",
                })
            serializer = TeacherDeSerializer(data=request_data)

            if serializer.is_valid():
                # 调用save()方法进行数据的保存  必须重写create()方法
                teacher_ser = serializer.save()
                print(teacher_ser)
                return Response({
                    "status": 200,
                    "message": "老师添加成功",
                    "results": TeacherSerializer(teacher_ser).data
                })
            else:

                return Response({
                    "status": 400,
                    "message": "员工添加失败",
                    # 保存失败的信息会包含在 .errors中
                    "results": serializer.errors
                })
