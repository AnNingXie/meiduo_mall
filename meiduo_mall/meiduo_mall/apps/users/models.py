from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 自定义用户模型类
class User(AbstractUser):
    # 手机号
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    # 自定义表名
    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    # 调试打印数据测试使用
    def __str__(self) -> str:
        return self.username
