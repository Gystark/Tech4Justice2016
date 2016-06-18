from django.shortcuts import render
from .models import Category, Reference, Issue, Question, Dictionary


def index(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html', {'categories': categories})


def view_category(request, category_name_slug):
    context = {}
    if request.method == "GET":
        category_searched = Category.objects.get(slug=category_name_slug)
        category_issues = Issue.objects.filter(category=category_searched)
        context['issues'] = category_issues
    return render(request, 'mainapp/issues.html', context)


def view_issue(request, issue_name_slug):
    context = []
    if request.method == "GET":
        issue_searched = Issue.objects.get(slug = issue_name_slug)
        # get the questions related to the issue
        issue_questions = Question.objects.filter(issue = issue_searched)

        for question in issue_questions:
            # get all the references related to this question
            references = Reference.objects.filter(question=question)
            context.append({'question': question, 'references': references})
        return render(request, 'mainapp/questions.html', {'context': context})

def search(request):
    if request.GET:
        search_term = request.GET['search-term']
    else:
        search_term = ''
    questions = Question.objects.filter(question__contains=search_term) or\
                Question.objects.filter(answer__contains=search_term)
    issues = Issue.objects.filter(name__contains=search_term)
    categories = Category.objects.filter(name__contains=search_term)
    return render(request, 'mainapp/search.html', {'issues': issues,'categories': categories, 'questions': questions})


def search_dictionary(request):
    if request.GET:
        search_term = request.GET['search-term']
    else:
        search_term = ''
    results = Dictionary.objects.filter(expression__contains=search_term) or\
              Dictionary.objects.filter(definition__contains=search_term)
    items = Dictionary.objects.all()
    return render(request, 'mainapp/dictionary.html', {'results': results, 'items': items})


def dictionary(request):
    items = Dictionary.objects.all()
    categories = Category.objects.all()
    return render(request, 'mainapp/dictionary.html', {'categories': categories, 'items': items})


def local_help(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/local_help.html', {'categories': categories})


def talk_to_someone(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/talk_to_someone.html', {'categories': categories})
