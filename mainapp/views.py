from django.shortcuts import render
from .models import Category, Reference, Issue, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request, 'mainapp/index.html', context)


def view_category(request, category_name_slug):
    return render(request, 'mainapp/category.html', {})

def get_issues(request):
    context = {}
    if request.is_ajax():
        category_searched = Category.objects.get(id=request.GET['category_id'])
        category_issues = Issue.objects.filter(category=category_searched)
        context['issues'] = category_issues
        return render(request, 'mainapp/issues.html', context)

    return HttpResponseRedirect('/')