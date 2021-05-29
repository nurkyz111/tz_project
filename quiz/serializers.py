from rest_framework import serializers
from .models import Quiz, Answer, Question


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['title']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id', 'answer_text', 'is_right'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question_title', 'answers']





