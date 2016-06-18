from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'text': 'Test text.'}
    return render(request, 'mainapp/index.html', context)