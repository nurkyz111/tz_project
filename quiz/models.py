from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Quiz title')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']

    def __str__(self):
        return self.title


class Question(models.Model):
    user = models.ManyToManyField(User, verbose_name='list of users')
    question_title = models.CharField(max_length=255, verbose_name='Question title')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)

    verbose_name = 'Answer'
    verbose_name_plural = 'Answers'
    ordering = ['id']

    def __str__(self):
        return self.answer_text


