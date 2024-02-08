from rest_framework import serializers

from tests import models as m


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Test
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_name'] = instance.course.title
        return representation


class TestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.TestUser
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_name'] = f'{instance.user.firstname} {instance.user.lastname}'
        representation['test_name'] = f'{instance.test.title}'

        questions_quantity = instance.questions.all().count()
        representation['questions'] = questions_quantity
        representation['percentage'] = f'{(instance.right_answers / questions_quantity):.2f}%'

        return representation
