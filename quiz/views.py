from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view

from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer


class QuizAPIView(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


@api_view(["POST"])
def answer_questions(request):
    data = request.data
    user = request.user
    dict_data = dict(data).items()

    if user.completed_test:
        return Response('dont cheat', status=status.HTTP_403_FORBIDDEN)
    else:
        for item in dict_data:
            question = item[0]
            answers = item[1][0]

            q = Question.objects.get(question_title=question)
            a = Answer.objects.get(answer_text=answers)

            if a.question != q:
                return Response('something is wrong', status=status.HTTP_400_BAD_REQUEST)

            if a.is_right:
                user.score += 1
                user.save()

        user.completed_test = True
        user.save()

    return Response('answered questions', status=status.HTTP_202_ACCEPTED)


class AnswerAPIView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


# class QuestionListAPIView(generics.ListAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer




