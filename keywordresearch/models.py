# myapp/models.py
from django.db import models


class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    related_keyword = models.CharField(max_length=255)

    def __str__(self):
        return self.related_keyword


class linkofenemy(models.Model):
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link


class KeywordsFinals(models.Model):
    field1 = models.CharField(max_length=100)

    def __str__(self):
        return self.field1


class KeywordsRank(models.Model):
    keyword = models.CharField(max_length=100)
    Mysite = models.CharField(max_length=100, default="-")
    myrank = models.CharField(max_length=100, default="-")

    rank_comparator1 = models.CharField(max_length=100, default="-")

    rank_comparator2 = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.keyword


class competitor(models.Model):
    url = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.url
