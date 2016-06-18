"""
Anything related to the admin page is here
"""
from django.contrib import admin
from mainapp.models import Question
from mainapp.models import Category
from mainapp.models import Issue
from mainapp.models import Reference
from mainapp.models import Dictionary


class CategoryAdmin(admin.ModelAdmin):
    """
    Populate the slug field in the Category model concurrently
    """
    prepopulated_fields = {'slug':('name',)}


class IssueAdmin(admin.ModelAdmin):
    """
    Populate the slug field in the Issue model concurrently
    """
    prepopulated_fields = {'slug':('name',)}


class QuestionAdmin(admin.ModelAdmin):
    """
    Populate the slug field in the Question model concurrently
    """
    prepopulated_fields = {'slug':('question',)}

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Reference)
admin.site.register(Dictionary)
