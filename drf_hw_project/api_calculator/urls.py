from django.urls import path

from api_calculator import views

urlpatterns = [
    path('v1/calculator/', views.CalculatorView.as_view()),
]
