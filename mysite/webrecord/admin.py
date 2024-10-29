from django.contrib import admin
from .models import AddrRecode

# Register your models here.

class AddrRecodeAdmin(admin.ModelAdmin):
    # 默认情况下django显示每个对象的str()返回的值，可以规定list_display来显示值
    list_display = ['id', 'description' ,'addr', 'create_time', 'last_modify_time', 'was_added_recently', 'views']
    list_filter = ["last_modify_time"]  # 增加过滤器，管理界面可以根据该过滤器来选择显示的数据库内容
    search_fields = ["description"] # 增加搜索框，后台使用like来查询数据
    fieldsets = [  # 字段集，用于显示具体某个记录的时候，按字段显示, 并且可以设置显示的样式
        ("Main", {"fields": ["description","addr", "views"]}),
        ("Date information", {"fields": ["create_time", "last_modify_time"], "classes": ["collapse"]})
    ]
    # inlines = [ChoiceInline] 用于在管理界面中嵌入关联模型的表单，使得在编辑一个模型对象的同时，可以编辑器关联的模型对象，通常用于一对一或一对多的关系

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


"""
class Order(models.Model):
    STATUS_CHOICES = [
        ('paid', '已支付'),
        ('unpaid', '未支付'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
"""
# SimpleListFilter用于自定义列表过滤功能，为模型管理页面添加自定义的过滤选项，使用户能更灵活地过滤数据
class OrderStatusFilter(admin.SimpleListFilter):
    title = '订单状态'  # 返回过滤器的标题，显示在过滤器的侧边栏中
    parameter_name = 'status' # 过滤器参数的名称，

    def lookups(self, request, model_admin): # 返回一个包含过滤选项的元组列表，每个元素包含两个元素：过滤值和显示的标签
        return [
            ('paid', '已支付'),
            ('unpaid', '未支付'),
        ]
    def queryset(self, request, queryset): # 根据用户选择的过滤选项，返回过滤后的查询集
        if self.value() == 'paid':
            return queryset.filter(status='paid')
        if self.value() == 'unpaid':
            return queryset.filter(status='unpaid')

"""    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = (OrderStatusFilter,)
    list_display = ('status', 'amount', 'created_at')
"""