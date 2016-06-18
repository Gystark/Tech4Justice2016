"""
All the models of the project are stored here.
"""
from django.db import models


class Category(models.Model):
    """
    Object representing a category in our database.
    """

    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    """
    Object representing different legal issues in our system
    """

    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Object representing the questions and answers of our system
    """

    question = models.CharField(max_length=128, unique=True)
    answer = models.TextField()
    issue = models.ForeignKey(Issue)

    def __str__(self):
        return self.question


class Reference(models.Model):
    """
    different references are stored here
    """

    reference = models.URLField()
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.reference

