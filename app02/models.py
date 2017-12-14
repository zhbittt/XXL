from django.db import models


class Role(models.Model):
    name = models.CharField(verbose_name="角色名", max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    role = models.ForeignKey(verbose_name="角色", to=Role)

    def __str__(self):
        return self.username