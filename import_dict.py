import os
import csv
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wasp.settings')
django.setup()
from mainapp.models import Dictionary


def save_data(data):
    Dictionary.objects.create(expression=data['expression'],
                              definition=data['definition'])

print('Starting dictionary upload...')
with open('mainapp/legal.txt', newline='', errors='ignore') as legalin:
    legalreader = csv.reader(legalin, delimiter=';')
    for row in legalreader:
        data = {
            'expression': row[0],
            'definition': row[1]
        }
        save_data(data)

print('Dictionary successfuly uploaded.')