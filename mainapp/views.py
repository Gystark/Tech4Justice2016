from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Reference, Issue, Question, Dictionary
from django.http import HttpResponseRedirect

def index(request):
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html', {'categories': categories})


def view_category(request, category_name_slug):
    context = {}
    if request.method == "GET":
        category_searched = Category.objects.get(slug=category_name_slug)
        category_questions = Question.objects.filter(issue__category=category_searched)
        context['questions'] = category_questions
        context['category_id'] = category_searched.id
    return render(request, 'mainapp/questions.html', context)

def search_questions(request):
    questions = []
    if request.is_ajax():
        search_term = request.GET['search_term']
        category_id = request.GET['category_id']
        category = Category.objects.get(id=category_id)
        issues = Issue.objects.filter(category=category)
        for issue in issues:
            results = Question.objects.filter(question__icontains=search_term, issue=issue) or \
                        Question.objects.filter(answer__icontains=search_term, issue=issue)
            for question in results:
                questions.append({'question': question, 'references': Reference.objects.filter(question=question)})

        obj = render(request, 'mainapp/questions_search.html', {'questions': questions, 'category_id': category_id})
        return obj


def search(request):
    if request.GET:
        search_term = request.GET['search-term']
    else:
        search_term = ''
    questions = Question.objects.filter(question__icontains=search_term) or\
                Question.objects.filter(answer__icontains=search_term)
    return render(request, 'mainapp/search.html', {'questions': questions})


def search_dictionary(request):
    if request.is_ajax():
        search_term = request.GET['search_term']
        results = Dictionary.objects.filter(expression__icontains=search_term) or \
                  Dictionary.objects.filter(definition__icontains=search_term)
        results_length = len(results)
        return render(request, 'mainapp/dictionary_search.html', {'items': results, 'length': results_length})


def dictionary(request):
    items = Dictionary.objects.all()
    paginator = Paginator(items, 25)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'mainapp/dictionary.html', {'items': items})


def local_help(request):
    return render(request, 'mainapp/local_help.html')


def talk_to_someone(request):
    return render(request, 'mainapp/talk_to_someone.html')


