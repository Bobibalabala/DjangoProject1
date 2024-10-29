from django.urls import re_path
from .views import LoginView, LoginForm

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(success_url='/admin.'), name='login', kwargs={'authentication_form': LoginForm})
]