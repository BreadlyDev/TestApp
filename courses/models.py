# from django.db import models
#
#
# def image_upload_path(instance, filename):
#     return f'courses/{instance.id}/images/{filename}'
#
#
# class Course(models.Model):
#     LANGUAGES = (
#         ('Кыргызский', 'Кыргызский'),
#         ('Русский', 'Русский'),
#         ('Английский', 'Английский'),
#     )
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='')
#     language = models.CharField(max_length=100, choices=LANGUAGES)
#     price = models.PositiveIntegerField()
#     description = models.TextField()
#
#     class Meta:
#         db_table = 'course'
#         verbose_name = 'Курс'
#         verbose_name_plural = 'Курсы'
#
#     def __str__(self):
#         return f'Курс {self.title}'
