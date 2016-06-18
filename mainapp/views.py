from django.shortcuts import render
from .models import Category, Reference, Issue, Question
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'mainapp/index.html', context)

def get_issues(request):
    if request.is_ajax():
        category_searched = Category.objects.get(id=request.GET['category_id'])
        category_issues = Issue.objects.filter(category=category_searched)
        print(category_issues)

    return HttpResponseRedirect('/')