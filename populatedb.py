"""
Populate the accounts table with dummy data.
"""
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wasp.settings')
django.setup()
from mainapp.models import *


def populate():
    family = Category.objects.get_or_create(name="Family Matters")[0]
    rights = Category.objects.get_or_create(name="Know Your Rights")[0]
    crime = Category.objects.get_or_create(name="Crime")[0]
    travelling = Category.objects.get_or_create(name='Traveling')[0]
    health = Category.objects.get_or_create(name='Health & Personal')[0]
    consumer = Category.objects.get_or_create(name='Money & Consumer')[0]

    family_issue1 = Issue.objects.get_or_create(name="Family issue 1", category=family)[0]
    family_issue2 = Issue.objects.get_or_create(name="Family issue 2", category=family)[0]

    family_issue1_question1 = Question.objects.get_or_create(question="Family question 1?", answer="Yes",
                                                         issue=family_issue1)[0]
    family_issue1_question2 = Question.objects.get_or_create(question="Family issue 2?",
                                                         answer="No", issue=family_issue2)[0]

    family_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=family_issue1_question1,
                                                                     name="Reference 1")
    family_issue1_question2_reference1 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=family_issue1_question2,
                                                                     name="Reference 2")

    rights_issue1 = Issue.objects.get_or_create(name="Rights issue 1", category=rights)[0]
    rights_issue2 = Issue.objects.get_or_create(name="Rights issue 2", category=rights)[0]

    rights_issue1_question1 = Question.objects.get_or_create(question="Rights question 1?", answer="Yes",
                                                         issue=rights_issue1)[0]
    rights_issue2_question2 = Question.objects.get_or_create(question="Rights issue 2?",
                                                         answer="No", issue=rights_issue2)[0]

    rights_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=rights_issue1_question1,
                                                                     name="Reference 1")
    rights_issue1_question2_reference1 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=rights_issue2_question2,
                                                                     name="Reference 2")
populate()