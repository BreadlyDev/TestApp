from rest_framework import generics, permissions, status
from rest_framework.response import Response

from . import models as m, serializers as s
from users import permissions as up


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


class TestUserCreateAPIView(generics.CreateAPIView):
    serializer_class = s.TestUserSerializer
    permission_classes = [up.IsStudent]

    def post(self, request, *args, **kwargs):
        data = self.request.data
        data['user'] = self.request.user

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {'message': 'Вы сдали тест'},
            **serializer.validated_data,
            status=status.HTTP_200_OK
        )


class TestUserListAPIView(generics.ListAPIView):
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]
