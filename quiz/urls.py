from django.urls import path
from .views import QuizAPIView, QuestionAPIView, AnswerAPIView, answer_questions

# app_name = 'quiz'

urlpatterns = [
    path('quiz/', QuizAPIView.as_view(), name='quiz'),
    path('question/', QuestionAPIView.as_view(), name='question'),
    path('answers/<int:pk>/', AnswerAPIView.as_view(), name='answers'),
    path('answer/', answer_questions),
]