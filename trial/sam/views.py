from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm, DistrictForm, StateForm
from .models import State, District, Student
from django.http import JsonResponse


from django.test import TestCase
from django.urls import reverse

# Create your views here.
def get_districts(request, state_id):
    districts = District.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(districts), safe=False)

def sam(request):
    return render(request, 'sam/sam.html')

def add_state(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state_list')
    else:
        form = StateForm()
    return render(request, 'sam/add_state.html', {'form': form})

def state_list(request):
    query = request.GET.get('q')
    if query:
        states = State.objects.filter(name__icontains=query)
    else:
        states = State.objects.all()

    # If AJAX request, return only the list
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'sam/_state_list.html', {'states': states})

    # Otherwise return full page
    return render(request, 'sam/state_list.html', {'states': states})


def update_state(request, pk):
    state=get_object_or_404(State, pk=pk)
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('state_list')
    else:
        form = StateForm(instance=state)
    return render(request, 'sam/update_state.html', {'form': form})

def state_delete(request, pk):
    state = get_object_or_404(State, pk=pk)
    state.delete()
    return redirect('state_list')

def list_districts(request):
    districts = District.objects.select_related('state').all()
    return render(request, 'sam/district_list.html', {'districts': districts})

def add_district(request):
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('district_list')
    else:
        form = DistrictForm()
    return render(request, 'sam/add_district.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'sam/add_student.html', {'form': form})


def student_list(request):
    q = request.GET.get('q')
    students = Student.objects.filter(name__icontains=q) if q else Student.objects.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'sam/_student_list.html', {'students': students})
    return render(request, 'sam/student_list.html', {'students': students})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'sam/edit_student.html', {'form': form, 'student': student})




class StudentViewsTest(TestCase):
    def test_student_list_page_loads(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student List")
