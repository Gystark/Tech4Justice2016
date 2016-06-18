from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'categories': ['family', 'rape', 'child abuse', 'drugs']}
    return render(request, 'mainapp/index.html', context)