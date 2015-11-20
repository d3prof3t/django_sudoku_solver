# solve/views.py

# Core Django Library Imports
from django.http import HttpResponse
from django.db import transaction

# Core Python Library Imports
import json

# Third Party Library Imports
from rest_framework.views import APIView

# App Specific Imports
from .models import SudokuSolverLog
from .serializers import SolverLogSerializer


class PostSudokuInput(APIView):

    def post(self, request):
        data = json.loads(request.data.get('post'))
        # create solvable sudoku list
        sudoku_list = self.create_sudoku_list(data)

        # serializer = SolverLogSerializer(sudoku_list)
        # print(serializer.data)

        # add the input to the db
        # input_log, created = SudokuSolverLog.objects.get_or_create(
            # input_sudoku=sudoku_list, result=0)
        # print(sudoku_list)
        # solve the sudoku list
        result = self.solve_sudoku(sudoku_list)
        print (result)
        # return HttpResponse(result)
        # return HttpResponse(sudoku_input_list)

    def create_sudoku_list(self, sudoku_list):
        sudoku_input_list = []
        for x in sudoku_list:
            for y in x:
                if y:
                    sudoku_input_list.append(y)
                else:
                    sudoku_input_list.append('-')
        return sudoku_input_list

    # def solve_sudoku(self, solvable_list):
    #     if isFull(solvable_list):
    #         print '\nSOLVED'
    #         return True
    #     else:
    #         trialCelli = getTrialCelli(solvable_list)
    #         trialVal = 1
    #         solution_found = False
    #         while (solution_found != True) and (trialVal < 10):
    #             print ('trial value', trialVal)
    #             if isLegal(trialVal, trialCelli, solvable_list):
    #                 solvable_list = setCell(
    #                     trialVal, trialCelli, solvable_list)
    #                 if hasSolution(solvable_list) == True:
    #                     solution_found = True
    #                     return True
    #                 else:
    #                     clearCell(trialCelli, solvable_list)
    #                     print '++'
    #                     trialVal += 1
    #     return solution_found
