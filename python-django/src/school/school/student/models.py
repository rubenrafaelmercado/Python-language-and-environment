from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
        
    def __str__(self):        
        return f'{self.name.title()}'


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    borning_date = models.DateField(null=True, blank=True)
    course = models.ForeignKey( Course, on_delete=models.CASCADE, null=True, blank=True  )
    
    def __str__(self):        
        return f'Apellido y nombre: {self.last_name.title()}, {self.first_name.title()}'



