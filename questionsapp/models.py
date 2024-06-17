from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.name}'

class Question(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.title}'
    

class Item(models.Model):
    title = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    correct = models.BooleanField()
    def __str__(self) -> str:
        return f'{self.question} - {self.title}'
    
class AnsweredQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.user.name} - {self.question.title} - {self.item.title} - {self.item.correct}'
    

