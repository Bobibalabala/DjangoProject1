from typing import Any
from django import forms
from .models import WebUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UsernameField
from django.utils.translation import gettext_lazy as _


class WebUserCreationForm(forms.ModelForm):
    """管理界面上创建用户的时候显示的表单"""
    password1 = forms.CharField(label=_("password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Enter password again"), widget=forms.PasswordInput)

    class Meta:
        # 绑定模型
        model = WebUser
        fields = ('email',)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("password do not match"))
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.source = "adminsite"
            user.save()
        return user
    

class WebUserChangeForm(UserChangeForm):
    class Meta:
        model = WebUser
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class WebUserAdmin(UserAdmin):
    form = WebUserChangeForm
    add_form= WebUserCreationForm
    list_display = (
        'id',
        'nickname',
        'username',
        'email',
        'last_login',
        'date_joined',
        'source'
    )
    list_display_links = ('id', 'username')
    ordering = ('-id', )
