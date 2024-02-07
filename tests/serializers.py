from rest_framework import serializers

from tests.models import Video, Test


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_name'] = instance.course.title
        return representation


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_name'] = instance.course.title
        return representation
