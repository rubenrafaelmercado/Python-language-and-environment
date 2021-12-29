from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
        
    def __str__(self):        
        return f'{self.name.title()}'


class Student(models.Model):

    STATUSES = [ 
        ('subscriber', 'Student subscriber'), 
        ('unsubscribed', 'Student unsubscribed'), 
        ('studying', 'Student studying')
        ]
    

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    borning_date = models.DateField(null=True, blank=True)
    course = models.ForeignKey( Course, on_delete=models.CASCADE, null=True, blank=True )
    status = models.CharField( max_length=30, choices=STATUSES, default='subscriber')
    
    def __str__(self):        
        return f'Full name: {self.last_name.title()}, {self.first_name.title()}'



