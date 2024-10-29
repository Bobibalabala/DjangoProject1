from django.shortcuts import render
from django.contrib import auth
from django.views.generic import FormView
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .forms import LoginForm
import logging

logger = logging.getLogger(__name__)


class LoginView(FormView):
    # 指定该视图类的表单显示
    form_class = LoginForm
    # 视图类渲染的模板
    template_name = "accounts/login.html"
    success_url = '/'
    # 用于指定重定向字段的名称，以便在表单提交后可以将用户重定向到指定的URL，通常用于登录和注销视图，以确保用户在完成操作后能够返回到他们之前访问的页面
    # 默认为next,这意味着用户在登录表单中可以看到一个隐藏的next参数，该参数的值是用户希望被重定向到的URL
    redirect_field_name = REDIRECT_FIELD_NAME
    login_ttl = 2626560  # 一个月


    # method_decorator是Django提供的一个工具，用于将装饰器应用到类视图的方法上
    @method_decorator(sensitive_post_parameters('password'))  # 标记视图函数中某些POST参数为敏感信息，这有助于在日志或错误报告中颖仓这些敏感信息
    @method_decorator(csrf_protect)  # 保护视图函数免受跨站请求伪造攻击
    @method_decorator(never_cache)  # 确保视图的响应不会被浏览器或其他中间件缓存
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)
    
    # 为模板提供上下文数据，即在渲染模板时传递给模板的变量，重写可以自定义传输给模板的数据，从而增强视图的功能
    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = '/'
        print('at get_context')
        kwargs['redirect_to'] = self.success_url
        return super().get_context_data(**kwargs)
    
    # 表单成功验证后被调用，主要用于执行一些额外的逻辑，如保存数据、重定向等。
    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)
        if form.is_valid():
            logger.info(self.redirect_field_name)
            # 标记用户为登录
            auth.login(self.request, form.get_user())
            if self.request.POST.get("remember"):
                self.request.session.set_expiry(self.login_ttl)
            return super().form_valid(form)
        else:
            # 将表单数据和上下文信息传递给一个模板，然后生成一个HTTP响应对象，用在表单验证失败时需要重新渲染表单页面的情况
            return self.render_to_response({'form': form})

    # 可以重写这个方法来动态生成重定向URL  
    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not url_has_allowed_host_and_scheme(url=redirect_to, allowed_hosts=[self.request.get_host()]):
            redirect_to = self.success_url
        return redirect_to