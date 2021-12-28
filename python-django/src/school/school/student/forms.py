from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from django.forms import ModelForm


#simple form
'''
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField()
    borning_date = forms.DateField()

    def save(self, commit=False):
        #raise Exception ( dir(self) )
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        borning_date = self.cleaned_data['borning_date']
        instance = Student(first_name = first_name, last_name = last_name, borning_date = borning_date)
        if commit:
            instance.save()
        

    #custom validation
    def clean_first_name (self):
        data = self.cleaned_data['first_name']
        if len(data) < 3:
            raise ValidationError ('Name is very small. Must be 3 characters or more')
        return data
'''

# matched to model form
class StudentForm (ModelForm):
    class Meta:
        model = Student
        #fields =['first_name' , 'last_name',  'borning_date']
        #fields = ['first_name' , 'last_name']
        fields =['first_name' , 'last_name', 'course', 'borning_date']

    #custom validation
    def clean_first_name (self):
        data = self.cleaned_data['first_name']
        if len(data) < 3:
            raise ValidationError ('Name is very small. Must be 3 characters or more')
        return data


# matched to 2 models form

