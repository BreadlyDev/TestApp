# from django.db import models
#
#
# class News(models.Model):
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='')
#     description = models.TextField()
#
#     class Meta:
#         db_table = 'news'
#         verbose_name = 'Новость'
#         verbose_name_plural = 'Новости'
#
#     def __str__(self):
#         return f'Новость {self.title}'
