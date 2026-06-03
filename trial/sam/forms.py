from django import forms
from .models import State, District, Student

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name', 'state']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'district', 'state', 'age', 'gender', 'course', 'photo']