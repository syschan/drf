from django.db import models


class Student(models.Model):#声明一个继承至Model的具体类Student
    # 模型字段
    name = models.CharField(max_length=100, verbose_name='姓名')
    sex = models.BooleanField(default=1, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    class_num = models.CharField(max_length=5, verbose_name='班级编号')
    description = models.TextField(max_length=100, verbose_name='个性签名')

    class Meta:
        db_table = "tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
