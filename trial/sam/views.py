from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm, DistrictForm, StateForm
from .models import State, District, Student
from django.http import JsonResponse

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
    if q:
        students = Student.objects.filter(name__icontains=q)
    else:
        students = Student.objects.all()
    return render(request, 'sam/student_list.html', {'students': students})

