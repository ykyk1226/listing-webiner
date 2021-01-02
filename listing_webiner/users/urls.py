from django.urls import path
from users.views.signup import Signup

app_name = 'users'
urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
]