from rest_framework import generics, permissions
from . import models as m, serializers as s


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionListAPIView(generics.ListAPIView):
    queryset = m.Question.objects.all()
    serializer_class = s.QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Question.objects.all()
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = s.AnswerSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerListAPIView(generics.ListAPIView):
    queryset = m.Answer.objects.all()
    serializer_class = s.QuestionSerializer


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Answer.objects.all()
    serializer_class = s.AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
