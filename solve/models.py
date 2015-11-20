# solve/models.py

# Core Django Library Imports
from django.db import models

# App Specific Imports
from sudoku_solver.models import TimeStampModel

RESULT_CHOICES = (
    (0, 'Incorrect'),
    (1, 'Correct'),
)


class SudokuSolverLog(TimeStampModel):

    """
    Docstring
    """
    input_sudoku = models.TextField(default='null')
    result = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']
