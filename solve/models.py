# solve/models.py

# Core Django Library Imports
from django.db import models

# App Specific Imports
from sudoku_solver.models import TimeStampModel


class SudokuSolverLog(TimeStampModel):

    """
    Docstring
    """
    input_sudoku = models.CharField(max_length=100, default='null')
    result = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']
