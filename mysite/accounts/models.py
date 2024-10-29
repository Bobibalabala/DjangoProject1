from django.db import models
from django.contrib.auth.models import AbstractUser  # 这个类是用户模型的抽象基类，通过继承该类可以添加额外的用户属性
from django.utils.timezone import now # 获取当前日期的函数
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class WebUser(AbstractUser):
    nickname = models.CharField(_('nick name'), max_length=100, blank=True)
    creation_time = models.DateTimeField(_('creation time'), default=now)
    last_modify_time = models.DateTimeField(_('modify time'), default=now)
    source = models.CharField(_('create source'), max_length=100, blank=True)

    def get_absolute_url(self):
        """模型类的一个约定，用于_url方法返回对象的URL，提供一个标准图URL，使得你的方式来获取某个对象的可以在模板中或其他地方详细页面的URL方便地连接到。"""
        return reverse('webuser:user_detail', kwargs={'username': self.username})
    
    def __str__(self) -> str:
        return self.username

    def get_full_url(self):
        """生成模型实例的完整url"""
        pass

    class Meta:
        """模型的元数据"""
        ordering = ['-id']  # 按照id进行默认的排序
        verbose_name = _('user')  # 管理界面该数据表的名称
        verbose_name_plural = verbose_name  # 当该数据表有多条记录时显示的该表的复数名
        get_latest_by = 'id'  # 按照哪个字段来获取模型最新的一个实例

        
