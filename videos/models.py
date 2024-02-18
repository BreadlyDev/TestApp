# from django.core.validators import FileExtensionValidator
# from django.db import models
#
#
# def video_upload_path(instance, filename):
#     return f'courses/{instance.course.id}/videos/{filename}'
#
#
# class Video(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     video = models.FileField(upload_to='', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
#
#     class Meta:
#         db_table = 'video'
#         verbose_name = 'Видео'
#         verbose_name_plural = 'Видео'
#
#     def __str__(self):
#         return f'Видео {self.title} по курсу {self.course.title}'
