from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.contrib.auth import get_user_model
from requests import get


class LoginForm(AuthenticationForm):
    """AuthenticationForm这个内置表单类，用于处理用户认证（登录）的功能，提供一些有用的方法和属性来简化用户登录表单的创建和处理"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置表单字段的显示格式，以及表单显示哪些字段
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder': "password", "class": "form-control"})


class RegisterForm(UserCreationForm):
    """UserCreationForm用于将模型直接映射到表单，从而简化表单的处理流程"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "username", "class": "form-control"})
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder': "email", "class": "form-control"})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'placeholder': "password", "class": "form-control"})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'placeholder': "repeat password", "class": "form-control"})

    class Meta:
        model = get_user_model()  # 表单关联的模型
        fields = ("username", "email") # 指定表单中需要显示的模型字段