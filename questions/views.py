from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models as m, serializers as s


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionListAPIView(generics.ListAPIView):
    queryset = m.Question.objects.all()
    serializer_class = s.QuestionSerializer

class QuestionsByTestAPIView(APIView):
    def get(self, request, pk):
        try:
            questions = m.Question.objects.filter(test=pk)
            serializer = s.QuestionSerializer(questions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

class AnswersByQuestionAPIView(APIView):
    def get(self, request, pk):
        try:
            questions = m.Answer.objects.filter(question=pk)
            serializer = s.AnswerSerializer(questions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
