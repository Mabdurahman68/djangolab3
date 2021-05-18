from django.http.response import HttpResponseRedirect
from osMansoura.forms import *
from django.shortcuts import render
from django.http import HttpResponse
from osMansoura.models import Student, Track

# Create your views here.

def home(request): 
    return HttpResponse("<h1>This is home page</h1>")

def getStudent(request, studentId): 
    student = Student.objects.get(id=studentId)
    context = {'student': student}
    return render(request, 'osMansoura/student.html', context)

def getAllStudents(request): 
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'osMansoura/students.html', context)

def createStudent(request):
    student_form = StudentForm()
    if request.method== "POST":
        student_form  = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect('/osMansoura/allstudents')
    context = {"student_form": student_form, "flag":True}
    return render(request,'osMansoura/create_student.html',context)


def editStudent(request, studentId):
    student = Student.objects.get(id=studentId)
    student_form = StudentForm(instance=student)
    if request.method== "POST":
        student_form  = StudentForm(request.POST ,instance=student)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect('/osMansoura/allstudents')
    context = {"student_form": student_form, "flag":False}
    return render(request,'osMansoura/create_student.html',context)

def deleteStudent(request, studentId):
    student = Student.objects.get(id=studentId)
    student.delete()
    return HttpResponseRedirect('/osMansoura/allstudents')

