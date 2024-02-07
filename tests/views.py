from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models as m, serializers as s


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = s.TestSerializer
    permission_classes = [permissions.IsAdminUser]


class TestListAPIView(generics.ListAPIView):
    queryset = m.Test.objects.all()
    serializer_class = s.TestSerializer


class TestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Test.objects.all()
    serializer_class = s.TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TestByCourseAPIView(APIView):
    def get(self, request, pk):
        try:
            questions = m.Test.objects.filter(course=pk)
            serializer = s.TestSerializer(questions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VideoCreateAPIView(generics.CreateAPIView):
    serializer_class = s.VideoSerializer
    permission_classes = [permissions.IsAdminUser]

class VideoByCourseAPIView(APIView):
    def get(self, request, pk):
        try:
            questions = m.Video.objects.filter(course=pk)
            serializer = s.VideoSerializer(questions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VideoListAPIView(generics.ListAPIView):
    queryset = m.Video.objects.all()
    serializer_class = s.TestSerializer


class VideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Video.objects.all()
    serializer_class = s.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
