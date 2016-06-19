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
    internet = Category.objects.get_or_create(name="Internet")[0]
    travelling = Category.objects.get_or_create(name='OUT & ABOUT')[0]
    health = Category.objects.get_or_create(name='Health & Personal')[0]
    crime = Category.objects.get_or_create(name='Crime')[0]

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

    rights_issue1_question1 = Question.objects.get_or_create(question="What happens if the police stop me on the street?", answer="The police may stop to talk to you for any number of reasons. They may just be looking for a general chat during their daily patrols.All officers take an interest in what you have to say, for example your thoughts on local issues and any problems you may be concerned about.However, they may also stop you if they have reason to suspect that you have committed or witnessed a crime or offence.If this happens, you must give your name and address if required to do so. If you are a suspect you may have to wait with the officer until your name and address has been checked.",
                                                         issue=rights_issue1)[0]
    rights_issue1_question2 = Question.objects.get_or_create(question="Are the Police allowed to search me?",
                                                         answer="A police officer can search you in one of two" +
"ways. The first way is with your consent. They will ask you if you agree to be searched, which you can refuse to allow. This is called a Consensual Search.A consensual search can be conducted by a police officer in the execution of their duty, but only with the consent of the individual being searched. Consensual searches will often be undertaken by officers as part of their general duties and they are done in order to prevent crime and to help keep people and communities safe.Alternatively you can be searched without your consent using legal powers available to Police Officers, provided certain requirements are met. This is called a Statutory Search. You cannot refuse to allow a Statutory Search and it is an offence to obstruct or hinder a police officer carrying out a Statutory Search. ", issue=rights_issue1)[0]
    rights_issue1_question3 = Question.objects.get_or_create(question="If the police want to search you, you are entitled to find ut why. ", answer="The reason for a Statutory Stop and Search, which could happen to you or any member of the public, is usually that the police officer has reasonable grounds to suspect that the person being searched is in unlawful possession of something such as controlled drugs, offensive weapon or stolen property.It should be pointed out that the police have the power to arrest people who are found to be in possession of knives and other types of weapons in public places when they don’t have either a reasonable excuse or lawful authority. Police officers will almost always enforce this legislation as knife crimes can have horrific and tragic consequences. Unfortunately young people are frequently involved both as the victims and sometimes the perpetrators of these crimes. Police also have powers to stop and search anyone they believe is a terrorist, or to prevent an act of terrorism.If the police want to search you, you are entitled to find out why. The following reasons are not good enough reasons to be searched: the officer knows that a person has previous convictions • the age of the person • the race of the person • the sex of the person There must be some specific information or intelligence that leads to the search. The Police can search your outer clothing and ‘pat’ you down in public. If the Police want to search beneath your outer clothing it must be done out of public view by an officer of your own sex. Intimate body searches can only be done if you have been detained for a Statutory Search and internal searches would require a warrant and can only be conducted by a medical professional.", issue=rights_issue1)[0]

    rights_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=rights_issue1_question1,
                                                                     name="Reference 1")
    rights_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=rights_issue1_question2,
                                                                     name="Reference 2")

    internet_issue1 = Issue.objects.get_or_create(name="internet issue 1", category=internet)[0]

    internet_issue1_question1 = Question.objects.get_or_create(question="Are there any issues I should be aware of, to safeguard myself when using social networking sites such as Facebook?", answer="People are being increasingly targeted by criminals via  ocial networking sites such as Facebook. You should be very careful about including any of the following personal information on your site: <ul><li> Name;</li><li>Address;</li><li>Telephone numbers / email addresses;</li><li>Education / employment information;</li><li>Photographs which may show your home and any valuables you may own;</li><li>Date of birth;</li><li>Status updates / comments which may state when you are not at home, when you are going on holiday, what expensive items you have recently bought etc.</li></ul> You should also be cautious about including 'friends of friends' in your privacy settings, as this effectively allows people who you do not know, to view your information. It is therefore advisable to allow only close personal friends and relatives to view your site. Strangers who request you to add them as a friend could be lying about their identity. A person could pretend to be someone else (e.g. pretending to be of the opposite sex, or adults pretending to be teenagers) in order to persuade another person to agree to meet up with them, when they actually have criminal intentions. Also, if you add someone who you do not know to your site, they may begin to ask you questions over time and aim conversations to particular subjects, in order to find out more information about you. If they already have your email address, they could log in to that account, using the information you have given them to answer your security questions, and reset your passwords. Once they have done this and have access to your personal emails, they could be gaining access to your bank details, online shopping accounts, paypal etc. and use these to take money from your accounts or buy goods in your name. Simply, to remain safe, check your security settings, be vigilant as to what information you post, and only accept people to your site who you know well. For further safety tips regarding social networking sites, please see the site in related information.",
                                                         issue=internet_issue1)[0]
    internet_issue1_question2 = Question.objects.get_or_create(question="internet issue 2?",
                                                         answer="No", issue=internet_issue1)[0]

    internet_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=internet_issue1_question1,
                                                                     name="Reference 1")
    internet_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=internet_issue1_question2,
                                                                     name="Reference 2")

    travelling_issue1 = Issue.objects.get_or_create(name="travelling issue 1", category=travelling)[0]

    travelling_issue1_question1 = Question.objects.get_or_create(question="travelling question 1?", answer="Yes",
                                                         issue=travelling_issue1)[0]
    travelling_issue2_question2 = Question.objects.get_or_create(question="travelling issue 2?",
                                                         answer="No", issue=travelling_issue1)[0]

    travelling_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=travelling_issue1_question1,
                                                                     name="Reference 1")
    travelling_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=travelling_issue2_question2,
                                                                     name="Reference 2")

    health_issue1 = Issue.objects.get_or_create(name="health issue 1", category=health)[0]

    health_issue1_question1 = Question.objects.get_or_create(question="health question 1?", answer="Yes",
                                                         issue=health_issue1)[0]
    health_issue2_question2 = Question.objects.get_or_create(question="health issue 2?",
                                                         answer="No", issue=health_issue1)[0]

    health_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=health_issue1_question1,
                                                                     name="Reference 1")
    health_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=health_issue2_question2,
                                                                     name="Reference 2")

    crime_issue1 = Issue.objects.get_or_create(name="crime issue 1", category=crime)[0]

    crime_issue1_question1 = Question.objects.get_or_create(question="crime question 1?", answer="Yes",
                                                         issue=crime_issue1)[0]
    crime_issue2_question2 = Question.objects.get_or_create(question="crime issue 2?",
                                                         answer="No", issue=crime_issue1)[0]

    crime_issue1_question1_reference1 = Reference.objects.get_or_create(reference="http://www.wwe.com",
                                                                     question=crime_issue1_question1,
                                                                     name="Reference 1")
    crime_issue1_question2_reference2 = Reference.objects.get_or_create(reference="http://facebook.com",
                                                                     question=crime_issue2_question2,
                                                                     name="Reference 2")
populate()