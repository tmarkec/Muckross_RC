# filepath: /Users/markotot/Desktop/VS CODE PROJECTS/Muckross_RC/MuckrossRC/home/views.py
from django.shortcuts import render


def home_view(request):
    return render(request, 'home/home.html')
