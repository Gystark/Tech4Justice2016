from django.shortcuts import render
from .models import Category, Reference, Issue, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse


def index(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html', {'categories': categories})


def view_category(request, category_name_slug):
    context = {}
    if request.method == "GET":
        category_searched = Category.objects.get(slug=category_name_slug)
        category_issues = Issue.objects.filter(category=category_searched)
        context['issues'] = category_issues
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request, 'mainapp/issues.html', context)


def view_issue(request, issue_name_slug):
    context = {}
    if request.method == "GET":
        issue_searched = Issue.objects.get(slug = issue_name_slug)
        issue_questions = Question.objects.filter(issue = issue_searched)
        context['questions'] = issue_questions
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request, 'mainapp/questions.html', context)


def search(request):
    if request.GET:
        search_term = request.GET['srch-term']
    else:
        search_term = ''
    categories = Category.objects.all()
    results = Question.objects.filter(question__contains=search_term) or \
              Question.objects.filter(answer__contains=search_term) or \
              Issue.objects.filter(name__contains=search_term) or \
              Category.objects.filter(name__contains=search_term)
    return render(request, 'mainapp/search.html', {'categories': categories, 'results': results})


def dictionary(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/dictionary.html', {'categories': categories})


def local_help(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/local_help.html', {'categories': categories})


def talk_to_someone(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/talk_to_someone.html', {'categories': categories})