from django.db import models

class Author(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(verbose_name="书名",max_length=32)
    content = models.CharField(verbose_name="简介",max_length=255)
    publish_time= models.DateField(verbose_name="出版时间")
    author = models.ForeignKey(verbose_name="作者",to=Author)

    def __str__(self):
        return self.title
class Publish(models.Model):
    title = models.CharField(verbose_name="出版社名称",max_length=32)
    addr = models.CharField(verbose_name="地址",max_length=128)

    def __str__(self):
        return self.title


