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

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'state', 'district', 'age', 'gender', 'course', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
