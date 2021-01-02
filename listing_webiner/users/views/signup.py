from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.views import generic
from users.forms.signupForm import SignupForm

class Signup(generic.CreateView):

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            user = get_user_model().objects.create_user(email=email, password=password1)
            user.save()
            user = authenticate(request, username=email, password=password1)
            login(request, user)
            return redirect(to='/lws/webiner')
        else:
            return render(request, 'users/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})