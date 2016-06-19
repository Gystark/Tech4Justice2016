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
    rights_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=rights_issue2_question2,
                                                                     name="Reference 2")

    crime_issue1 = Issue.objects.get_or_create(name="crime issue 1", category=crime)[0]
    crime_issue2 = Issue.objects.get_or_create(name="crime issue 2", category=crime)[0]

    crime_issue1_question1 = Question.objects.get_or_create(question="crime question 1?", answer="Yes",
                                                         issue=crime_issue1)[0]
    crime_issue2_question2 = Question.objects.get_or_create(question="crime issue 2?",
                                                         answer="No", issue=crime_issue2)[0]

    crime_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=crime_issue1_question1,
                                                                     name="Reference 1")
    crime_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=crime_issue2_question2,
                                                                     name="Reference 2")

    travelling_issue1 = Issue.objects.get_or_create(name="travelling issue 1", category=travelling)[0]
    travelling_issue2 = Issue.objects.get_or_create(name="travelling issue 2", category=travelling)[0]

    travelling_issue1_question1 = Question.objects.get_or_create(question="travelling question 1?", answer="Yes",
                                                         issue=travelling_issue1)[0]
    travelling_issue2_question2 = Question.objects.get_or_create(question="travelling issue 2?",
                                                         answer="No", issue=travelling_issue2)[0]

    travelling_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=travelling_issue1_question1,
                                                                     name="Reference 1")
    travelling_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=travelling_issue2_question2,
                                                                     name="Reference 2")

    health_issue1 = Issue.objects.get_or_create(name="health issue 1", category=health)[0]
    health_issue2 = Issue.objects.get_or_create(name="health issue 2", category=health)[0]

    health_issue1_question1 = Question.objects.get_or_create(question="health question 1?", answer="Yes",
                                                         issue=health_issue1)[0]
    health_issue2_question2 = Question.objects.get_or_create(question="health issue 2?",
                                                         answer="No", issue=health_issue2)[0]

    health_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=health_issue1_question1,
                                                                     name="Reference 1")
    health_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=health_issue2_question2,
                                                                     name="Reference 2")

    consumer_issue1 = Issue.objects.get_or_create(name="consumer issue 1", category=consumer)[0]
    consumer_issue2 = Issue.objects.get_or_create(name="consumer issue 2", category=consumer)[0]

    consumer_issue1_question1 = Question.objects.get_or_create(question="consumer question 1?", answer="Yes",
                                                         issue=consumer_issue1)[0]
    consumer_issue2_question2 = Question.objects.get_or_create(question="consumer issue 2?",
                                                         answer="No", issue=consumer_issue2)[0]

    consumer_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=consumer_issue1_question1,
                                                                     name="Reference 1")
    consumer_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=consumer_issue2_question2,
                                                                     name="Reference 2")
populate()