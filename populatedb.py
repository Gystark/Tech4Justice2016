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
    c4 = Category.objects.get_or_create(name="drugs")[0]

    c1_issue1 = Issue.objects.get_or_create(name="child abuse", category=c1)
    c1_issue2 = Issue.objects.get_or_create(name="bad kids", category=c1)

populate()