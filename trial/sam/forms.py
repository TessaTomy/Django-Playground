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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'district', 'state', 'age', 'gender', 'course', 'photo']
        
