from rest_framework import generics, permissions

from . import models as m, serializers as s


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = s.TestSerializer
    permission_classes = [permissions.IsAdminUser]


class TestListAPIView(generics.ListAPIView):
    serializer_class = s.TestSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('pk')
        queryset = m.Test.objects.filter(course=course_id)
        return queryset


class TestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Test.objects.all()
    serializer_class = s.TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TestUserListAPIView(generics.ListAPIView):
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestUserCreateAPIView(generics.CreateAPIView):
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoCreateAPIView(generics.CreateAPIView):
    serializer_class = s.VideoSerializer
    permission_classes = [permissions.IsAdminUser]


class VideoListAPIView(generics.ListAPIView):
    serializer_class = s.VideoSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('pk')
        queryset = m.Video.objects.filter(course=course_id)
        return queryset


class VideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Video.objects.all()
    serializer_class = s.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
