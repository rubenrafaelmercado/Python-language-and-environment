#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from .models import Student


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def add_student(request):        
    #raise Exception(first_name)    
    Student.objects.create(first_name=request.GET.get('first_name', '-'),
                          last_name=request.GET.get('last_name', '-'))    
    response = {'status': 'OK'}
    return JsonResponse(response)
    

def get_students(request):    
    Students = Student.objects.all()
    html = '<html><body><h1>Students<H1>'
    for item in Students:
        html += f'<p><a href="/students/{item.id}">{item.last_name}, {item.first_name}</a></p>'
    html += '</body></html>'
    return HttpResponse(html)


def get_student(request, id_student):    
    student = Student.objects.get(pk=id_student)
    #raise Exception(student.first_name.title())
    html = '<html><body><h1>Students<H1>'
    html += f'<p>Apellido: {student.last_name}</p>'
    html += f'<p>Nombre: {student.first_name}</p>'
    html += f'<p>Nacimiento: {student.borning_date}</p>'
    html += '</body></html>'
    return HttpResponse(html)


