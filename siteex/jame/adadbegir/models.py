# models.py
from django.db import models

class UserInput(models.Model):
    text_field = models.TextField()
    number_field = models.IntegerField()

    def __str__(self):
        return f"{self.text_field} - {self.number_field}"

class MyModel(models.Model):
    text_field = models.TextField()
    number_field = models.IntegerField()

    def __str__(self):
        return f"{self.text_field} - {self.number_field}"
