"""
Anything related to the admin page is here
"""
from django.contrib import admin
from mainapp.models import Question
from mainapp.models import Category
from mainapp.models import Issue
from mainapp.models import Reference

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Issue)
admin.site.register(Reference)

