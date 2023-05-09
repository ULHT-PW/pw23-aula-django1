from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index_view(request):

    linguagens = ['JS', 'Python']

    context = {
        'ano': datetime.now().year,
        'hora': datetime.now().hour,
        'linguagens': linguagens,
    }

    return render(request, 'pw/index.html', context)



def about_view(request):
    
    context = {
        'ano': datetime.now().year
    }
    return render(request, 'pw/about.html', context)