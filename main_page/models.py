from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from . import validators as v


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields['role'] = 'Администратор'
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    ROLES = (
        ('Учитель', 'Учитель'),
        ('Студент', 'Студент')
    )

    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    patronymic = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=ROLES, default=ROLES[1][1], null=True)

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.role} {self.firstname} {self.lastname}'

    def save(self, *args, **kwargs):
        if self.password and not str(self.password).startswith(('pbkdf2_sha256$', 'bcrypt')):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Profile(models.Model):
    LANGUAGES = (
        ('Кыргызский', 'Кыргызский'),
        ('Русский', 'Русский'),
        ('Английский', 'Английский'),
    )

    SEX = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    language = models.CharField(max_length=50, choices=LANGUAGES)
    _class = models.CharField(max_length=4, validators=[v.validate_class])
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50, choices=SEX)
    phone = models.CharField(max_length=20, validators=[v.validate_phone])
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль студента {self.user.lastname} {self.user.firstname}'


def image_upload_path(instance, filename):
    return f'courses/{instance.id}/images/{filename}'


class Course(models.Model):
    LANGUAGES = (
        ('Кыргызский', 'Кыргызский'),
        ('Русский', 'Русский'),
        ('Английский', 'Английский'),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    language = models.CharField(max_length=100, choices=LANGUAGES)
    price = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'course'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'Курс {self.title}'


def video_upload_path(instance, filename):
    return f'courses/{instance.course.id}/videos/{filename}'


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')

    class Meta:
        db_table = 'video'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'Видео {self.title} по курсу {self.course.title}'


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')
    previous_test = models.OneToOneField('self', on_delete=models.PROTECT, related_name='next_test', null=True, blank=True)

    class Meta:
        db_table = 'test'
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'Тест {self.title} по курсу {self.course.title}'


class UserTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests')
    right_answers = models.PositiveIntegerField()

    class Meta:
        db_table = 'test_user'
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'

    def __str__(self):
        return f'Тест {self.test.title} пройденный студентом {self.user.firstname} {self.user.lastname}'


class Question(models.Model):
    title = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        db_table = 'questions'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'Вопрос {self.title}'


class Answer(models.Model):
    title = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    class Meta:
        db_table = 'answers'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        response = f'Ответ {self.title} на вопрос {self.question.title}'
        return f'Верный {response}' if self.correct else response


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_answers')

    class Meta:
        db_table = 'user_answers'
        verbose_name = 'Ответ студента'
        verbose_name_plural = 'Ответы студента'

    def __str__(self):
        return (f'Ответ студента {self.user.username} '
                f'на вопрос {self.answer.question.title} '
                f'по тесту {self.answer.question.test.title}')


class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'Новость {self.title}'
