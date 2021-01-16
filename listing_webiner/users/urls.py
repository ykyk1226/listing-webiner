from django.urls import path
from users.views.signup_view import SignupView

app_name = 'users'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]