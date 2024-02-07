from django.urls import path
from . import views

urlpatterns = [
    path('create', views.QuestionCreateAPIView.as_view()),
    path('all', views.QuestionListAPIView.as_view()),
    path('<int:pk>', views.QuestionDetailAPIView.as_view()),

    path('create', views.AnswerCreateAPIView.as_view()),
    path('all', views.AnswerListAPIView.as_view()),
    path('<int:pk>', views.AnswerDetailAPIView.as_view()),
]
