from django.shortcuts import render
from .models import Category, Reference, Issue, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse


def index(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html', {'categories': categories})


def view_category(request, category_name_slug):
    categories = Category.objects.all()
    return render(request, 'mainapp/category.html', {'categories': categories})

def get_issues(request):
    context = {}
    if request.is_ajax():
        category_searched = Category.objects.get(id=request.GET['category_id'])
        category_issues = Issue.objects.filter(category=category_searched)
        context['issues'] = category_issues
        return render(request, 'mainapp/issues.html', context)

    return HttpResponseRedirect('/')


def search(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/search.html', {'categories': categories})


def dictionary(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/dictionary.html', {'categories': categories})


def local_help(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/local_help.html', {'categories': categories})


def talk_to_someone(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/talk_to_someone.html', {'categories': categories})