
from django.contrib.auth.models import AbstractUser
from django.db import models

# from quiz.models import Question
# from quiz.models import Question


class User(AbstractUser):
    # question = models.ManyToManyRel(Question, related_name='questions')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=18)
    date_joined = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField(default=0)
    completed_test = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


