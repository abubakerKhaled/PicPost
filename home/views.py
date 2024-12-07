from django.shortcuts import render



def home(request):
    context = {
        'section': 'dashboard',
    }
    return render(request, 'home/index.html', context)