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
