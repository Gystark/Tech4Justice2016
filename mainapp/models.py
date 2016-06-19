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
    slug = models.SlugField()
    photo = models.ImageField(upload_to='category_photos')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


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
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question


class Reference(models.Model):
    """
    different references are stored here
    """

    name = models.CharField(max_length=100, default="")
    reference = models.URLField()
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.reference


class Dictionary(models.Model):
    """
    Model for the legal terms dictionary.
    expression: a legal expression
    definition: an  explanation for the exprezsion
    """

    expression = models.CharField(max_length=100)
    definition = models.CharField(max_length=500)

    def __str__(self):
        return self.expression

    class Meta:
        verbose_name_plural = 'dictionaries'
