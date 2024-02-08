from django.core.validators import FileExtensionValidator
from django.db import models

from courses.models import Course
from main.settings import TEST_VIDEO_FOLDER
from users.models import User


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        db_table = 'test'
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'Тест {self.title} по курсу {self.course.title}'


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to=TEST_VIDEO_FOLDER, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'video'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'Видео {self.title} по курсу {self.course.title}'


class TestUser(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests')
    is_passed = models.BooleanField(default=False)
    right_answers = models.PositiveIntegerField()

    class Meta:
        db_table = 'test_user'
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'
