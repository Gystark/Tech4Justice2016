"""
Populate the accounts table with dummy data.
"""
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wasp.settings')
django.setup()
from mainapp.models import *

def populate():
    c1 = Category.objects.get_or_create(name="faimily")[0]
    c2 = Category.objects.get_or_create(name="rape")[0]
    c3 = Category.objects.get_or_create(name="drugs")[0]

    c1_issue1 = Issue.objects.get_or_create(name="child abuse", category=c1)[0]
    c1_issue2 = Issue.objects.get_or_create(name="bad kids", category=c1)[0]

    c1_issue1_question1 = Question.objects.get_or_create(question="My father beats me, what to do?", answer="Yes",
                                                         issue=c1_issue1)[0]
    c1_issue1_question2 = Question.objects.get_or_create(question="My father talks shit to me, what to do",
                                                         answer="You can't do anything, she's your mother", issue=c1_issue1)[0]

    c1_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=c1_issue1_question1,
                                                                     name="WWE WEBSITE")
    c1_issue1_question2_reference1 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=c1_issue1_question2,
                                                                     name="FACEBOOK")
populate()