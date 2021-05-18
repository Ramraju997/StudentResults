from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from StudentDetails.models import Students
from StudentDetails.serializer import StudentSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        studentDetails = Students.objects.all()
        student_serializer = StudentSerializer(studentDetails, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    elif request.method == 'POST':
        Student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=Student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def addmarks(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return JsonResponse({'message': 'Student details does not exist'}, status=status.HTTP_404_NOT_FOUND)
    Student_data = JSONParser().parse(request)
    student_serializer = StudentSerializer(student, data=Student_data)
    if student_serializer.is_valid():
        student_serializer.save()
        return JsonResponse(student_serializer.data)
    return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getpercentage(request):
    count = Students.objects.all().count()
    A = Students.objects.filter(marks__gte='91',marks__lte='100').count()
    B= Students.objects.filter(marks__gte='81',marks__lte='90').count()
    C= Students.objects.filter(marks__gte='71',marks__lte='80').count()
    F=Students.objects.filter(marks__lte='54').count()
    print(count)
    print(A)
    print(B)
    print(C)
    print(F)
    print((count - F) / count)

    return JsonResponse({"Distinction Percentage": A/count, "Firstclass Percentage": B+C/count,"Pass percentage":(count - F)/count}, status=status.HTTP_200_OK)
@api_view(['GET'])
def results(request):
    count = Students.objects.all().count()
    A = Students.objects.filter(marks__gte='91',marks__lte='100').count()
    B= Students.objects.filter(marks__gte='81',marks__lte='90').count()
    C= Students.objects.filter(marks__gte='71',marks__lte='80').count()
    D= Students.objects.filter(marks__gte='61',marks__lte='70').count()
    E=Students.objects.filter(marks__gte='61',marks__lte='55').count()
    F=Students.objects.filter(marks__lte='54').count()

    print(count)
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)
    print((count - F) / count)

    return JsonResponse({"Total number of students": count, "A grade Students": A,"B grade Students":B,"C grade Students":C,"D grade Students":D,"E grade Students":E,"F grade Students":F}, status=status.HTTP_200_OK)

