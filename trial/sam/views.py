from django.shortcuts import render

# Create your views here.
def sam_home(request):
    return render(request, 'sam/sam_home.html')