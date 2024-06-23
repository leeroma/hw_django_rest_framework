from django.urls import path

from api_calculator import views

urlpatterns = [
    path('calculator/', views.CalculatorView.as_view(), name='calculator'),
]
