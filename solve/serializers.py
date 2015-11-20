# solve/serializers.py

# User Specific Imports
from .models import SudokuSolverLog

# Third Party Library Imports
from rest_framework import serializers


class SolverLogSerializer(serializers.ModelSerializer):

    """
    Docstring
    """
    class Meta:
        model = SudokuSolverLog
        fields = ('input_sudoku', )
