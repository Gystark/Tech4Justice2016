from django.shortcuts import render
from mainapp.models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {'text': 'Test text.', 'categories': categories}
    return render(request, 'mainapp/index.html', context)