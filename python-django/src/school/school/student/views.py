from django.http import HttpResponse, JsonResponse
import datetime
from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

@login_required
def add_student(request):        
    #raise Exception(first_name)    
    Student.objects.create(first_name=request.GET.get('first_name', '-'),
                          last_name=request.GET.get('last_name', '-'))    
    response = {'status': 'OK'}
    return JsonResponse(response)
    

@login_required
def get_students(request):    
        
    '''
    #Whithout template
    html = '<html><body><h1>Students<H1>'
    for item in Students:
        html += f'<p><a href="/students/{item.id}">{item.last_name}, {item.first_name}</a></p>'
    html += '</body></html>'
    return HttpResponse(html)
    '''

    #With a template
    #return render(request, 'list.html', context = {'students' : students})

    #With base template
    #return render(request, 'list-content.html', context = {'students' : students})

    #whith forms
    form = StudentForm()
    validation_error = False
    if request.method == 'POST':
        form = StudentForm(request.POST)        
        if form.is_valid():
            form.save(commit = True)
        else:
            validation_error = True
    
    students = Student.objects.all()

    return render(request, 
            'list-content.html',
            context = {
                'students' : students,
                'form' : form,
                'validation_error' : validation_error,
            })

@login_required
def get_student(request, id_student):    
    
    student = Student.objects.get(pk=id_student)
        
    #debug var
    #raise Exception(student.first_name.title())

    '''
    #Whithout template
    html = '<html><body><h1>Students<H1>'
    html += f'<p>Apellido: {student.last_name}</p>'
    html += f'<p>Nombre: {student.first_name}</p>'
    html += f'<p>Nacimiento: {student.borning_date}</p>'
    html += '</body></html>'
    return HttpResponse(html)    '''

    #With a template
    #return render(request, 'detail.html', context = {'student' : student})


    #whith forms
    form = StudentForm( instance=student )
    validation_error = False    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)                
        if form.is_valid():
            form.save(commit = True)
        else:
            validation_error = True

    return render(request, 
            'detail.html',
            context = {
                'student' : student,
                'form' : form,
                'validation_error' : validation_error,
            })






