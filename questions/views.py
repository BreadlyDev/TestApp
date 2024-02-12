from rest_framework import generics, permissions
from rest_framework.response import Response

from . import models as m, serializers as s
from users import permissions as custom_permissions


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = s.QuestionSerializer

    def get_queryset(self):
        test_id = self.kwargs.get('pk')
        queryset = m.Question.objects.filter(test=test_id)
        return queryset


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Question.objects.all()
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = s.AnswerSerializer
    permission_classes = [custom_permissions.IsTeacher]


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = s.AnswerSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        queryset = m.Answer.objects.filter(question=question_id)
        return queryset


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Answer.objects.all()
    serializer_class = s.AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserAnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = s.UserAnswerSerializer
    permission_classes = [custom_permissions.IsStudent]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UserAnswerListAPIView(generics.ListAPIView):
    serializer_class = s.UserAnswerSerializer

    def get_queryset(self):
        test_id = self.kwargs.get('test_pk')
        user_id = self.kwargs.get('user_pk')
        queryset = m.UserAnswer.objects.filter(user=user_id, answer__question__test_id=test_id)
        return queryset


class UserAnswerDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = m.UserAnswer.objects.all()
    serializer_class = s.UserAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
