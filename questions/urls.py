from django.urls import path
from . import views

urlpatterns = [
    path('create', views.QuestionCreateAPIView.as_view()),
    path('all', views.QuestionListAPIView.as_view()),
    path('test/<int:pk>', views.QuestionsByTestAPIView.as_view()),
    path('<int:pk>', views.QuestionDetailAPIView.as_view()),

    path('answer/create', views.AnswerCreateAPIView.as_view()),
    path('answer/all', views.AnswerListAPIView.as_view()),
    path('answer/<int:pk>', views.AnswerDetailAPIView.as_view()),
    path('answer/question/<int:pk>', views.AnswersByQuestionAPIView.as_view()),
]
