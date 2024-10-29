from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(_('creation time'), default=now)
    last_modify_time = models.DateTimeField(_('modify time'), default=now)


class AddrRecode(BaseModel):
    """
    status = models.CharField(
        _('status'), # 该字段在表中实际的名称
        max_length=1, # 最大长度
        choices=STATUS_CHOICES, # 表示status只能接受的选项
        default='p', # 默认值
        null=False, # 不能为NULL值
        blank=False, # 不能为空
        verbose_name=_('status'), # 在用户界面中显示字段名，如果未指定将自动使用字段名的首字母大写形式。
        )
    """
    # _()函数是django的国际化函数，用于标记字符串为可翻译的字符串，

    description = models.CharField(_('descrption'), max_length=128, unique=True)
    addr = models.URLField(_('address'), unique=True)
    views = models.PositiveIntegerField(_('views'), default=0) # 浏览量
    
    def __str__(self) -> str:
        return self.description
    
    # admin.display 装饰器用于自定义模型字段在 Django 管理界面中的显示方式。 可以让布尔值的显示为打勾图标
    @admin.display(boolean=True, ordering="create_time", description="added recently?")
    def was_added_recently(self):
        now = timezone.now()
        return now >= self.create_time >= timezone.now() - timezone.timedelta(days=1)
    
    # 内嵌套类Meta,用于定义模型的元数据，影响模型的行为、管理界面的显示、数据表的创建等
    class Meta:
        # db_table = "werecord" # 指定数据库中的表名称
        ordering = ["create_time", "-description"] # 指定按哪些字段进行排序，按列表中的先后优先排，加-表示倒序
        unique_together = [['description', 'addr']] # 唯一约束，指定多个字段的组合必须是唯一的
        # permission = [ ('can_view_special_reports', 'Can view special reports'), ] # 定义模型的自定义权限
        app_label = 'webrecord' # 指定模型所属于的应用
        # 指定模型的单数和复数形式， 如不指定，则管理界面上表的名称为Addr recorde
        # verbose_name = 'Article'
        # verbose_name_plural = 'Articles'
        default_permissions = ('add', 'change', 'delete', 'view') # 指定模型的默认权限
        # 指定该模型的索引，以优化查询性能
        # indexes = [models.Index(fields=['name', 'category']), ]
        get_latest_by = 'id' # get_latest_by，它用于指定在查询模型对象时，默认使用哪个字段来获取最新的记录。
        
    def viewed(self):
        """用于标记浏览量，当获取该对象的时候，可以调用本函数用于增加该对象的浏览量"""
        self.views += 1
        self.save(update_fields=['views'])


        
    
