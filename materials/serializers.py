from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import VideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [VideoValidator(field='video_link')]
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_count', many=True, read_only=True)
    sign_up = SerializerMethodField(source='subscription_course', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_count', many=True, read_only=True)
    subscription_course = serializers.SerializerMethodField()
    sign_up = SubscriptionSerializer(source='subscription_course', many=True, read_only=True)

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_sign_up(self, instance):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user).filter(course=instance).exists()

    class Meta:
        model = Course
        fields = ('lessons', 'title', 'description', 'lesson_count', 'image', 'owner', 'subscription_course',)
