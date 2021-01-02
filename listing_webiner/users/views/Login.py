from django.shortcuts import redirect
from django.contrib.auth import login
from users.models.custom_user import CustomUser
from users.forms.loginForm import LoginForm
from django.views.generic.base import View

class Login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = CustomUser.objects.get(email=email)
            login(request, user)
            return redirect('/lws/webiner')
        return redirect(to='/users/login')

    def get(self, request, *args, **kwargs):
        return redirect(to='/users/login')