from msilib.schema import ListView
from multiprocessing import context
from statistics import mode
from turtle import title
from unicodedata import name
from django.shortcuts import render
from .models import Student
from .forms import StudentForm 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from core.serializers import Studentserializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Student






# Create your views here.
def home(request):
    form = StudentForm()
    stu = Student.objects.all()
    context = {'form':form, 'stu':stu}
    return render(request, 'core/home.html',context)

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            course = request.POST['course']
            print('student id',sid)

            if(sid == ''):
                s = Student(name=name, email=email, course=course)
            else:
                s = Student(id=sid, name=name, email=email, course=course)
            s.save()

            stu = Student.objects.values()
            student_data = list(stu)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s = Student.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print('Student ID',id)
        student = Student.objects.get(pk=id)
        student_data = {'id':student.id, 'name':student.name, 'email':student.email, 'course':student.course}
        return JsonResponse(student_data)


def searchbar(request):
    if request.method=="GET":
        form = StudentForm()
        search=request.GET.get('search')
        post=Student.objects.all().filter(name=search)
        return render(request, 'core/searchbar.html', {'post':post, 'form':form, 'search':search})

    
        
  
        

                    # class studentViewSet(APIView):
                    #     def get(get,request):
                    #         query=Student.objects.all()
                    #         serializers_class=Studentserializers(query,many=True)
                    #         return Response(serializers_class.data)


                        # def get(request,pk):
                        #     query=Student.objects.get(id=pk)
                        #     serializers_class=Studentserializers(query)
                        #     return Response(serializers_class.data)


# def student_list(request):
#     stu=Student.objects.all()   
#     serializer=Studentserializers(stu, many=True)  
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# def student_detail(request,pk):
#     stu=Student.objects.get(id=pk)
#     serializer=Studentserializers(stu)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

                        # query_set to get single data (method= 2) using the Jsonresponse
                        # def student_detail(request,pk):
                        #     stu=Student.objects.get(id=pk)
                        #     serializer=StudentSerializers(stu)
                        #     return JsonResponse(serializer.data)

    

class ItemViews(APIView):
    def post(self, request):
        serializer = Studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Student.objects.get(id=id)
            serializer = Studentserializers(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Student.objects.all()
        serializer = Studentserializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Student.objects.get(id=id)
        serializer = Studentserializers(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, id):
        item = Student.objects.get(id=id)
        print(Student)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})  
  
  
