"""
All the models of the project are stored here.
"""
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """
    Object representing a category in our database.
    """

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Issue(models.Model):
    """
    Object representing different legal issues in our system
    """

    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Issue, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Object representing the questions and answers of our system
    """

    question = models.CharField(max_length=128, unique=True)
    answer = models.TextField()
    issue = models.ForeignKey(Issue)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Category, self).save(*args, **kwargs)

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

