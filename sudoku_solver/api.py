# sudoku_solver/views.py

# Core Django Library Imports
from django.conf.urls import url, patterns

# App Specific Imports
from solve import views as solver_views

urlpatterns = patterns(
    'solve.views',
    url(r'^api/v1/input/', solver_views.PostSudokuInput.as_view(),
        name='input-sudoku-api'),
)
