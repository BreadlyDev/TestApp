from rest_framework import serializers

from questions import models as m


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Answer
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.UserAnswer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['question'] = instance.answer.question.id
        representation['question_title'] = instance.answer.question.title
        representation['test'] = instance.answer.question.test.id
        representation['test_title'] = instance.answer.question.test.title
        return representation