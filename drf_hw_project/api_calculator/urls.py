from django.urls import path

from api_calculator import views

urlpatterns = [
    path('v1/add/', views.AddView.as_view()),
    path('v1/multiply/', views.MultiplyView.as_view()),
    path('v1/subtract/', views.SubtractView.as_view()),
    path('v1/divide/', views.DivideView.as_view()),
]
