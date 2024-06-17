from django.shortcuts import render
from .models import Question, AnsweredQuestion
from django.db import models

def question_list(request, user_id):
    questions = Question.objects.annotate(
        answered_by_user=models.Exists(
            AnsweredQuestion.objects.filter(user_id=user_id, question=models.OuterRef('pk'))
        )
    )

    context = {'questions': questions, 'user_id': user_id}
    return render(request, 'question_list.html', context)