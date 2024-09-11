from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def salon(request):
    return render(request,'salon.html')