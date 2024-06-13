from django.urls import path

from api_calculator import views

urlpatterns = [
    path('v1/add/', views.AddView.as_view()),
]
