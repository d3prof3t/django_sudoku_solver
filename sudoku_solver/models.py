# sudoku_solver/models.py

from django.db import models


class TimeStampModel(models.Model):

    """
    Docstring
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
