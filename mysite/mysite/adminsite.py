from django.contrib.admin import AdminSite
from webrecord.models import AddrRecode
from webrecord.admin import AddrRecodeAdmin
from accounts.models import WebUser
from accounts.admin import WebUserAdmin

class MysiteAdmin(AdminSite):
    # 主标题 
    index_title = "管理"
    # 管理界面header标签里的内容
    site_header = "网站数据库管理"
    # title标签内容
    site_title = 'mysite'

    def __init__(self, name: str = 'admin') -> None:
        super().__init__(name)

admin_site = MysiteAdmin(name='yangbo')
admin_site.register(AddrRecode, AddrRecodeAdmin)
admin_site.register(WebUser, WebUserAdmin)