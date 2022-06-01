from django.urls import path
from calculator.views import get_recipe

urlpatterns = [
    path('<recipe>/', get_recipe)
]