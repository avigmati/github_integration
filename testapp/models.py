from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100)


class AnotherModel(models.Model):
    title = models.CharField(max_length=100)
