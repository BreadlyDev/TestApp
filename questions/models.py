# from django.db import models
#
# from my_tests import models as m
# from users.models import User
#
#
# class Question(models.Model):
#     title = models.CharField(max_length=255)
#     test = models.ForeignKey(m.Test, on_delete=models.CASCADE, related_name='questions')
#
#     class Meta:
#         db_table = 'questions'
#         verbose_name = 'Вопрос'
#         verbose_name_plural = 'Вопросы'
#
#     def __str__(self):
#         return f'Вопрос {self.title}'
#
#
# class Answer(models.Model):
#     title = models.CharField(max_length=255)
#     correct = models.BooleanField(default=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
#
#     class Meta:
#         db_table = 'answers'
#         verbose_name = 'Ответ'
#         verbose_name_plural = 'Ответы'
#
#     def __str__(self):
#         response = f'Ответ {self.title} на вопрос {self.question.title}'
#         return f'Верный {response}' if self.correct else response
#
#
# class UserAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answers')
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_answers')
#
#     class Meta:
#         db_table = 'user_answers'
#         verbose_name = 'Ответ студента'
#         verbose_name_plural = 'Ответы студента'
#
#     def __str__(self):
#         return (f'Ответ студента {self.user.username} '
#                 f'на вопрос {self.answer.question.title} '
#                 f'по тесту {self.answer.question.test.title}')
