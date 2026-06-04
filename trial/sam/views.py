from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm, DistrictForm, StateForm
from .models import State, District, Student

# Create your views here.
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