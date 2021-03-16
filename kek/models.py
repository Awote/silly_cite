from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class User(models.Model):
    login_user = models.CharField(verbose_name='Логин',max_length=50, primary_key=True,unique=True)
    password = models.CharField(verbose_name='Пароль',max_length=41)
    First_Name = models.TextField(verbose_name='Имя')
    user_bio = models.TextField(verbose_name='Фамилия')

#     Date_of_Birth = models.DateField(verbose_name='День рождения')
#     MALE =(
#         (1,'Мужской'),
#         (2,'Женский')
#           )
#     Male = models.IntegerField(verbose_name='Пол',choices=MALE)
#     email = models.EmailField(verbose_name='Email',max_length='256')
# # class Video(models.Model):
#     id_video = models.IntegerField(verbose_name='ID_VIDEO')
#     login_user = models.ForeignKey(verbose_name='Логин',on_delete=models.CASCADE)
#     path_video = models.FilePathField(path='')

