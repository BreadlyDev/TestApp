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
    queryset = m.TestUser.objects.all()
    serializer_class = s.TestUserSerializer
    permission_classes = [up.IsStudent]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id

        r_answers = data['right_answers']
        test = m.Test.objects.filter(pk=data['test']).first()
        questions = test.questions.count()

        if self.queryset.filter(user=request.user.id, test=data['test']).exists():
            return Response(
                {'message': 'Вы уже проходили этот тест'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if r_answers > questions:
            return Response(
                {'message': 'Количество ответов не может быть больше количества вопросов'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'message': 'Вы сдали тест',
                **serializer.data,
             },
        )


class TestUserListAPIView(generics.ListAPIView):
    queryset = m.TestUser.objects.all()
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'Учитель':
            return self.queryset

        return self.queryset.filter(user=user)


class TestUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.TestUser.objects.all()
    serializer_class = s.TestUserSerializer
    permission_classes = [permissions.IsAuthenticated]
