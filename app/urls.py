from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/end', views.count_result, name='count_result')
]